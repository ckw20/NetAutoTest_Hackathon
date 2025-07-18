import sys
import os
import json
from openai import OpenAI
# 将项目根路径加入到 sys.path 中
sys.path.insert(0, "/root/NetAutoTest")
from src.utils.extract_api import *
from src.script_generator.common import *
import yaml
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
from tqdm import tqdm

def load_prompt_template(yaml_path: str):
    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


def split_intent_code(lines: str):

    # 提取以 # 开头的注释行为 intent，直到遇到非注释行为止
    intent_lines = []
    code_started = False
    code_lines = []

    for line in lines:
        stripped = line.strip()
        if not code_started and stripped.startswith("#"):
            intent_lines.append(line.replace("#",""))
        else:
            code_started = True
            code_lines.append(line)

    intent = "".join(intent_lines).strip()
    code = "".join(code_lines).strip()

    return intent,code

def translate_intent(url: str, key: str, intent: str,model: str):
    client = OpenAI(
        api_key=key, 
        base_url=url,
    )
    messages = [
        {"role": "system", "content": "You are a translator. Please translate the following Chinese text into English accurately, keeping technical terms.Output only the English intention, without any extra content."},
        {"role": "user", "content": intent}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content.strip()


def llm(model, intent, code, api_list, prompt_template,key,url ):
    client = OpenAI(
        api_key=key, 
        base_url=url,
    )

    # # 加载并填充 prompt
    # prompt_template = load_config(prompt_path)

    prompt = prompt_template.format(intent=intent, code=code, api_list=";\n".join(api_list))
    print(">> prompt:\n",prompt)
    messages = [{"role": "system", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    content = response.choices[0].message.content
    print("==== LLM Output ====")
    print(content)
    return content,prompt



def match_api_descriptions(content, api_json_path):

    # 读取 JSON 文件中的所有 API 定义
    with open(api_json_path, 'r', encoding='utf-8') as f:
        api_data = json.load(f)

    api_functions=list(get_testerlib_base_functions("".join(content), 'TesterLibrary.base'))

    matched_apis = []

    for entry in api_data:
        full_name = entry.get("method_name", "")
        func_name = full_name.split('.')[-1]  # 取函数名最后一级

        if func_name in api_functions:
            matched_apis.append(
                func_name+":"+entry.get("description", ""),
            )

    return matched_apis






def llm_with_retry(model, intent, code, functions, prompt_template, api_key,base_url,retries=10, wait_sec=10):
    for attempt in range(1, retries + 1):
        try:
            return llm(model, intent, code, functions, prompt_template,api_key,base_url)
        except Exception as e:
            print(f"⚠️ 第 {attempt} 次调用 llm 失败：{e}")
            if attempt < retries:
                print(f"⏳ 正在等待 {wait_sec} 秒后重试...")
                time.sleep(wait_sec)
            else:
                print("❌ 已达最大重试次数，跳过该用例。")
                return None, None





def load_examples(root_dir):
   
    py_file_list = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith('.py'):
                py_file_list.append(os.path.join(dirpath, f))

    return py_file_list


def load_cepri_dev_new(root_dir):
    py_file_list = []
    subdirs = [entry for entry in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, entry))]
    for entry in subdirs:
        case_dir = os.path.join(root_dir, entry)
        main_path = os.path.join(case_dir, 'main.py')
        if os.path.exists(main_path):
            py_file_list.append(main_path)
        else:
            print(f"跳过：{main_path} 不存在")
            continue
            
    return py_file_list



def process_one_case(args):
    """ 单个用例处理逻辑（可被并行调用） """
    py_path, api_json_path, prompt_template, model ,api_key,base_url= args
    try:
        with open(py_path, 'r', encoding='utf-8') as f:
            content = f.readlines()

        functions = match_api_descriptions(content, api_json_path)
        intent, code = split_intent_code(content)

        intent_en = translate_intent(base_url, api_key,intent,model)

        rewrite_intent, prompt = llm_with_retry(model, intent_en, code, functions, prompt_template,api_key,base_url)

        if rewrite_intent is None:
            return None

        return {
            "path": py_path,
            "intent": intent,
            "intent_en": intent_en,
            "code": code,
            "functions": functions,
            "rewrite_intent": rewrite_intent,
            "prompt": prompt
        }

    except Exception as e:
        print(f"❌ 处理失败：{py_path}，错误：{e}")
        return None


def load_config(yaml_path: str) -> dict:
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    start_time=time.time()
    json_path="/root/NetAutoTest/data/rewrite_results/all_python_results_english.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    listed=[item["path"] for item in data]

    config_path = "/root/NetAutoTest/src/script_generator/intent_rewrite/prompts/example_process_config.yaml"
    config = load_config(config_path)


    prompt_path = '/root/NetAutoTest/src/script_generator/intent_rewrite/prompts/prompt_example_process_english_v2.yaml'
    prompt_template=load_config(prompt_path)["prompt_template"]

    # 加载用例路径列表
    examples_py_file_list = load_examples(config["examples_root_dir"])
    cepri_dev_new_py_file_list = load_cepri_dev_new(config["cepri_dev_new_root_dir"])
    py_file_list = examples_py_file_list + cepri_dev_new_py_file_list
    py_file_list_=[]
    for i in py_file_list:
        if i not in listed:
            py_file_list_.append(i)

    print(">> examples_py_file_list 个数 :", len(examples_py_file_list))
    print(">> cepri_dev_new_py_file_list 个数 :", len(cepri_dev_new_py_file_list))
    print(">> 用例总个数 :", len(py_file_list))
    print(">> 用例总个数 :", len(py_file_list_))

    # ✅ 构造并行参数
    task_args = [(path, config["api_json_path"], prompt_template, config["model"],config["api_key"],config["base_url"]) for path in py_file_list_]

    results = []
    with ProcessPoolExecutor(max_workers=8) as executor:  # 设置并发进程数
        futures = [executor.submit(process_one_case, arg) for arg in task_args]

        for future in tqdm(as_completed(futures), total=len(futures), desc="🚀 并行处理中"):
            result = future.result()
            if result:
                results.append(result)

    # 保存最终结果
    output_json_path=config["output_json_path"]          
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    end_time=time.time()
    elapsed=end_time-start_time
    print(f"\n✅ 并行处理完成，总耗时：{elapsed:.2f} 秒，共成功处理 {len(results)} 个用例，结果保存到：{output_json_path}")
    



# if __name__ == "__main__":
#     path = '/root/NetAutoTest/data/ref_projects/cepri-dev-new/Testcase/tc_6_7_6/main.py'
#     prompt_path = '/root/NetAutoTest/src/script_generator/intent_rewrite/prompts/intent_rewrite.yaml'  #  prompt.yaml 的路径
    
#     model = "deepseek-r1"

#     content = open(path, 'r', encoding='utf-8').readlines()

#     api_json_path="/root/NetAutoTest/data/parsed_documents/API_docs/last_llm_result_with_names.json"
#     functions = match_api_descriptions(content,api_json_path)

#     intent, code = split_intent_code(content)

#     print(">> Extracted Intent:\n", intent)
#     print(">> Extracted Code:\n", code)
#     print(">> Extracted API List:\n", functions)

#     rewrite_intent,prompt=llm(model, intent, code, functions, prompt_path)


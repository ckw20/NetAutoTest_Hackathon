import yaml
from openai import OpenAI


def load_config(yaml_path: str) -> dict:
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def build_zh_few_shot_prompt(top_examples) -> str:
    prompt = "以下是历史中具有代表性的网络测试子任务改写示例：\n\n"
    for idx, (example, score) in enumerate(top_examples, 1):
        prompt += f"🔹 示例 {idx}（综合相似度: {score * 100:.4f}）\n"
        prompt += example.to_prompt() + "\n\n"
    prompt += "请参考以上示例，将新的测试意图改写为标准化子任务列表。只输出子任务列表即可。\n"
    return prompt


def build_en_few_shot_prompt(top_examples) -> str:
    prompt = "Below are representative examples of rewritten network testing subtasks from history:\n\n"
    for idx, (example, score) in enumerate(top_examples, 1):
        prompt += f"🔹 Example {idx} (Combined Similarity: {score * 100:.4f})\n"
        prompt += example.to_prompt() + "\n\n"
    prompt += "Please refer to the examples above and rewrite the new test intent into a standardized list of subtasks. Output only the subtask list.Do not include any additional content.\n"
    return prompt

def build_few_shot_prompt(top_examples, config) -> str:
    if config["language"]=="en":
        return build_en_few_shot_prompt(top_examples)
    else:
        return build_zh_few_shot_prompt(top_examples)


def llm(model, prompt, key, url, retry=3):
    client = OpenAI(api_key=key, base_url=url)
    messages = [{"role": "system", "content": prompt}]
    for i in range(retry):
        try:
            response = client.chat.completions.create(model=model, messages=messages)
            return response.choices[0].message.content, prompt
        except Exception as e:
            if i == retry - 1:
                raise e
            time.sleep(2 ** i)  # exponential backoff


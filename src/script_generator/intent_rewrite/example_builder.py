import json
import re


def clean_text(text: str) -> str:
    text = re.sub(r"[-=]{3,}", "", text)
    text = re.sub(r"[#*]+\s*", "", text)
    text = re.sub(r"[\r\n\t]+", " ", text)
    return text.strip()


class ExampleEntry:
    def __init__(self, data: dict,language="zh"):
        self.data = data
        self.intent = data["intent"]
        self.intent_en = data.get("intent_en", "")
        self.path = data["path"]
        self.rewrite_intent = data.get("rewrite_intent", "")
        self.tc_no = self.path
        self.language = language


    def to_prompt(self):
        
        if self.language=="en":
            prompt = f"### Example Path: {self.tc_no}\n"
            prompt += f"# Original Test Intent:\n{self.intent_en.strip()}\n"
            prompt += "# Rewritten Subtask List:\n"

        else:
            prompt = f"### 示例路径: {self.tc_no}\n"
            prompt += f"# 原始测试意图:\n{self.intent.strip()}\n"
            prompt += "# 改写后的子任务列表:\n"
        
        try:
            parsed = json.loads(self.rewrite_intent) if isinstance(self.rewrite_intent, str) else self.rewrite_intent
            for key in sorted(parsed.keys(), key=lambda x: int(''.join(filter(str.isdigit, x)))):
                prompt += f"{key}: {parsed[key]}\n"
        except Exception as e:
            prompt += f"[⚠️ rewrite_intent 解析失败: {e}]\n{self.rewrite_intent}\n"
        return prompt.strip()




def load_examples_from_json(config):

    if config.get("language")=="en":
        json_path=config["en_example_json"]
    else:
        json_path = config["zh_example_json"]
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]

    return [ExampleEntry(item, language=config.get("language", "zh")) for item in data]

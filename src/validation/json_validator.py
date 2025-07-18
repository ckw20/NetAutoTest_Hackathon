# 根据json模板检查给定json文件格式是否正确

import json
import jsonschema
from jsonschema import validate

import logging

logger = logging.getLogger(__name__)

def load_json(file_path):
    """加载 JSON 文件"""
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json(json_data, schema):
    """验证 JSON 数据是否符合模式"""
    try:
        validate(instance=json_data, schema=schema)
        logger.info("JSON 数据符合模板规范。")
        return True
    except jsonschema.exceptions.ValidationError as e:
        logger.error("JSON 数据不符合模板规范。")
        logger.error(f"错误信息: {e.message}")
        return False

def check_json_format(json_str):
    """
    检查 JSON 格式是否正确
    :param json_string: 需要检查的 JSON 字符串
    :return: (bool, str) - 是否有效以及错误信息（如果有的话）
    """
    try:
        json.loads(json_str)
        print("✅ JSON 字符串格式正确")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误：{e}")
        return False
    
if __name__ == "__main__":
    # valid_json = '{"name": "Alice", "age": 25, "city": "New York"}'
    # invalid_json = '{"name": "Alice", "age": 25, "city": "New York"'  # 缺少右括号

    # print(check_json_format(valid_json))  # 应返回 (True, "JSON 格式正确")
    # print(check_json_format(invalid_json))  # 应返回 (False, "JSON 格式错误: ...")s

    # # 加载 JSON 文件和模板文件
    # json_file_path = "/root/NetAutoTest/data/testcases/exp_res/2025-03-11-14-10-04_qwen-max-latest_rfc2328_9.5/rfc2328_9.5.json"
    # schema_file_path = "/root/NetAutoTest/data/testcases/examples/testcase_template_with_topology_schema.json"
    json_file_path = "/root/NetAutoTest/data/testcases/exp_res/2025-03-11-14-10-04_qwen-max-latest_rfc2328_9.5/rfc2328_9.5_testpoints.json"
    schema_file_path = "/root/NetAutoTest/data/testcases/examples/testcase_point_template_schema.json"
    # json_data = load_json(json_file_path)
    json_data = {"test_case_points": []}
    schema = load_json(schema_file_path)

    # json_data = {
    #     "name": "John",
    #     "ge": 30,
    #     "ciy": "New York"}

    # schema = {
    #     "type": "object",
    #     "properties": {
    #         "name": {"type": "string"},
    #         "age": {"type": "number"},
    #         "city": {"type": "string"}
    #     },
    #     "required": ["name", "age"]
    # }


    # 验证 JSON 数据
    # print(validate_json(json_data, schema))
    data = json.loads("""{"valid": false, "comments": "Your comments here"}""")
    schema = json.loads("""{"type":"object","properties":{"valid":{"type":"boolean"},"comments":{"type":"string"}},"required":["valid","comments"]}""")
    print(validate_json(data, schema))

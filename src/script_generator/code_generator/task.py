import os, json, shutil
from ..common import load_json, copy_between

class Task:
    def __init__(self,
                 task: dict,
                 dir: str | None = None,
                 comments: dict | None = None,
                 result_code: str | None = None):
        self.task = task
        self.dir = dir
        if result_code is None:
            self.id = self.task["id"]
            self.title = self.task["title"]
            self.objective = self.task["objective"]
            self.test_reference = self.task.get("test_reference", None)
            self.steps = self.task["steps"]
            self.tags = self.task.get("tags", None)
        else:
            self.id = None
            self.title = None
            self.objective = None
            self.test_reference = None
            self.topology = None
            self.steps = None
            self.tags = None

        if self.dir is not None:
            self.cfg = load_json(os.path.join(self.dir, 'cfg.json'))
            self.tc_no = self.cfg["tc_no"]
            self.testbed = load_json(os.path.join(self.dir, 'testbed.json'))
        else:
            self.cfg = None
            self.testbed = None
            self.tc_no = task["tc_no"]
        self.comments = comments
        self.result_code = result_code

    def to_task_description(self) -> str:
        prompt = ""
        prompt += "# =================================================================================\n"
        if self.objective is not None:
            prompt += "# Objective  : " + self.objective + "\n#\n"

        assert self.steps is not None and len(self.steps) > 0
        prompt += "# Step       : "
        for step_id in range(len(self.steps)):
            step = self.steps[step_id]
            if step_id > 0: prompt += "#              "
            prompt += "Test Step" + str(step_id + 1) + ": " + step["description"] + "\n"

        prompt += "# Criteria   : "
        expect_result_id = 0
        for step_id in range(len(self.steps)):
            step = self.steps[step_id]
            if step["expected_result"] is not None and len(step["expected_result"]) > 0:
                expect_result_id += 1
                if expect_result_id > 0: prompt += "#              "
                prompt += "Expected Result" + str(expect_result_id) + ": " + step["expected_result"] + "\n"

        if self.tags is not None and len(self.tags) > 0:
            prompt += "# Tags       : " + (str(self.tags) if len(self.tags) > 1 else self.tags[0]) + "\n"

        if self.title is not None: pass
        prompt += "# =================================================================================\n"
        return prompt

    def to_prompt(self) -> str:
        prompt = ""
        if self.result_code is not None:
            prompt += "# The following is an example, including a task description and corresponding sample code for your reference:\n"
            prompt += "# The following is the task description:\n"
            prompt += self.task["prompt"] + "\n"
            prompt += "# The following is the sample code corresponding to the above task description:\n"
            prompt += "```python\n"
            prompt += self.result_code
            prompt += "```\n"
            prompt += "# The above is an example containing a task description and corresponding code.\n"
        else:
            prompt += "# The following is the task description for which you need to generate the corresponding code this time:\n"
            prompt += self.to_task_description()
            if self.cfg is not None:
                prompt += "The following are parameters you may use. In the generated code, refer to other examples, you can use the cfg dictionary to reference these parameters:" + str(self.cfg) + "\n"
            if self.testbed is not None:
                prompt += "The following are testbed-related parameters. In the generated code, refer to other examples, you can use the testbed dictionary to reference these parameters:" + str(self.testbed) + "\n"
            prompt += "# The above is the task description and related parameters for which you need to generate the corresponding code this time. You need to follow the above task description and refer to other examples to generate the corresponding code.\n"

        return prompt

    def to_api_query(self):
        return self.to_task_description()

    def to_example_query(self):
        return self.to_task_description()

    def to_example_corpus(self):
        return self.task["prompt"]


def load_task(task_dir: str, file_name: str):
    task: dict = load_json(os.path.join(task_dir, file_name))
    return Task(
        task=task["test_cases"][0] if "test_cases" in task else task,
        dir=task_dir,
        comments=task["comments"] if "comments" in task.keys() else None,
        result_code=None
    )

def move_the_fucking_cfg_testbed_device_setup_and_teardown_between_dir(
    all_file_in_one_dir: str, xet_repo_root_dir: str,testbed: dict, cfg: dict, from_src_to_dst: bool):
    tc_no = cfg['tc_no']
    duts = cfg['dut'] # ["DeviceA","DeviceB","DeviceC"]
    dut_cfgs: list[str] = cfg['dut_cfg'] # ["DeviceA_Setup","DeviceA_Teardown","DeviceB_Setup","DeviceB_Teardown","DeviceC_Setup","DeviceC_Teardown"]
    for dut in duts:
        if dut not in testbed['dut'].keys(): continue
        dut_type = testbed['dut'][dut]['dut_type'] # huawei_ce6881, etc
        command_path = os.path.join(xet_repo_root_dir, 'command', dut_type, tc_no)
        for dut_cfg in dut_cfgs:
            if dut_cfg.startswith(dut):
                copy_between(all_file_in_one_dir, command_path, dut_cfg + '.txt', from_src_to_dst)
    tc_no_path = os.path.join(xet_repo_root_dir, cfg['type'], tc_no)
    copy_between(all_file_in_one_dir, tc_no_path, 'main.py', from_src_to_dst)
    copy_between(all_file_in_one_dir, tc_no_path, 'cfg.json', from_src_to_dst)
    copy_between(all_file_in_one_dir,  os.path.join(xet_repo_root_dir, cfg['type']), 'testbed.json', from_src_to_dst)


def load_examples(path: str, no_cfg: bool = False):
    examples: list[Task] = []

    if no_cfg ==  True:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    content = open(os.path.join(root, file)).read()
                    # split by 'from' or 'import'
                    result_code_pos = min(content.find("from"), content.find("import"))    
                    task = Task(
                        task={"prompt": content[:result_code_pos], "tc_no": file.split('.')[0]},
                        result_code=content[result_code_pos:]
                    )
                    examples.append(task)
    else:
        testbed_path = os.path.join(path, 'Testcase/testbed.json')
        testbed = load_json(testbed_path)
        for root, dirs, files in os.walk(path):
            if 'main.py' in files and 'cfg.json' in files:
                content = open(os.path.join(root, 'main.py')).read()
                cfg = load_json(os.path.join(root, 'cfg.json'))
                # split by 'from' or 'import'
                result_code_pos = min(content.find("from"), content.find("import"))
                assert result_code_pos != -1

                move_the_fucking_cfg_testbed_device_setup_and_teardown_between_dir(
                    root, path, testbed, cfg, from_src_to_dst=False
                )

                task = Task(
                    task={"prompt": content[:result_code_pos]},
                    dir=root,
                    result_code=content[result_code_pos:]
                )
                examples.append(task)
    return examples
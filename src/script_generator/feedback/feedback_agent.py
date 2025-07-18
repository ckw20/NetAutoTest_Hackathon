import os, json, shutil
from ..common import create_file_and_write
from ..retriever import ExperienceRetriever
import logging
logger = logging.getLogger(__name__)

class FeedbackResponse:
    def __init__(self,
                 run_response: dict,
                 syntax_response: dict | None = None,
                 hl_response: dict | None = None):
        self.run_response = run_response
        if run_response is not None:
            self.run_status = run_response["status"] # success or error
            self.run_message = run_response["message"]
            self.run_verdict = run_response["output"]["verdict"] # pass or fail
            self.run_errInfo = run_response["output"]["errInfo"]
            self.run_info = run_response["output"]["info"]
            self.run_excuteInfo = run_response["output"]["excuteInfo"] if "excuteInfo" in run_response["output"] else ""

        self.syntax_response = syntax_response
        if syntax_response is not None:
            self.syntax_status = syntax_response["status"] # success or error
            self.syntax_info = syntax_response["info"]

        self.hl_response = hl_response
        if hl_response is not None:
            self.hl_status = hl_response["status"] # success or error
            self.hl_info = hl_response["info"]
        
        self.response = {
            "run_response": run_response,
            "syntax_response": syntax_response,
            "hl_response": hl_response
        }

    def success(self):
        if self.hl_response is not None:
            return True if self.hl_status == "success" else False
        if self.run_response is not None:
            return True if (self.run_status == "success" and self.run_verdict == "pass") else False
        if self.syntax_response is not None:
            return True if self.syntax_status == "success" else False
        logger.error("In FeedbackAgent.success(): No hl_response, run_response and syntax_response.")
        return True

    def to_prompt(self):
        prompt = ""
        if self.syntax_response is not None:
            if self.syntax_status == "error":
                prompt += f"The generated code has the following syntax errors: {self.syntax_info}\n"
        if self.run_response is not None:
            if self.run_status == "error":
                prompt += f"Runtime error occurred, error message: {self.run_errInfo} (detailed run info: {self.run_errInfo})\n"
            elif self.run_verdict == "fail":
                prompt += f"The actual run result does not match the expectation, error message: {self.run_errInfo} (detailed run info: {self.run_errInfo})\n"
        if self.hl_response is not None:
            if self.hl_status == "error" and self.hl_info != "":
                prompt += f"Manual review feedback: {self.hl_info}"
        return prompt

class FeedbackAgent:
    def __init__(self,
                 request_api: callable,
                 script_path: str,
                 experience_retriever: ExperienceRetriever,
                 HL_enable: bool = False):
        self.request_api = request_api
        self.script_path = script_path
        os.makedirs(script_path)
        self.experience_retriever = experience_retriever
        self.HL_enable = HL_enable
        self.iter = 0

    def _syntax_response(self, dir: dict):
        return {
            "status": "No response",
            "info": "No syntax check implemented yet."
        }

    def _HL_response(self, dir: str, code: str, run_response: dict | None, expert_exps: list[dict] | None = None):
        assert self.HL_enable == True
        info = input(f"Enter your feedback (the generated code, run response, and history expert advice can be found in {dir}):\
                     \n\tinput 'success' for success,\
                     \n\tinput int or list[int] (index start from 0) for directly using expert experience,\
                     \n\tpress enter for no feedback,\
                     \n\tinput file path for using the file content as feedback,\
                     \n\tor input anything else for using the input as feedback\
                     \n>>>>> ")
        if info == "": return None
        if info == "success":
            return {
                "status": "success",
                "info": ""
            }
        if info.isdigit() or (info.startswith("[") and info.endswith("]")):
            if info.startswith("[") and info.endswith("]"):
                info = [int(x.strip()) for x in info[1: -1].split(",") if x.strip()]
            else: info = [int(info)]
            suggestions = []
            for exp_index in info:
                assert expert_exps is not None, "expert_exps should not be None when using expert experience."
                assert 0 <= exp_index and exp_index < len(expert_exps), f"Invalid index {exp_index} for expert experience."
                suggestions.append(expert_exps[exp_index]["suggestion"])
            return {
                "status": "error",
                "info": f"Expert experience from similar past issues: {', '.join(suggestions)}"
            }
        if info != "" and os.path.exists(info): info = open(info, "r").read()
        if run_response is not None:
            self.experience_retriever.add_experience({
                "error_info": run_response["output"]["errInfo"],
                "run_info": run_response["output"]["info"],
                "suggestion": info,
                "code": code
            })
        return {
            "status": "error",
            "info": info
        }

    # The dir should contains main.py, cfg.json, testbed.json, Device*_*.txt
    def request(self, code: str, dir: str):
        self.iter += 1
        temp_dir = os.path.join(self.script_path, f'iter_{self.iter}')
        shutil.copytree(dir, temp_dir)
        create_file_and_write(os.path.join(temp_dir, 'main.py'), code)

        assert self.request_api is not None, "request_api should be a callable function."
        run_response: dict = self.request_api(temp_dir)
        if run_response is not None:
            logger.info(f'>>> The generated code is saved in: {os.path.join(temp_dir, "main.py")}')
            logger.info(f'>>> The run response is saved in: {os.path.join(temp_dir, "response.json")}')
        syntax_response = self._syntax_response(temp_dir)

        expert_exps = self.experience_retriever.retrieve({
            "error_info": run_response["output"]["errInfo"] if run_response is not None else ""
            # "run_info": run_response["output"]["info"] if run_response is not None else "",
            # "code": code
        })
        expert_exps = [exp.to_dict() for exp in expert_exps]
        for i in range(len(expert_exps)): expert_exps[i]["index"] = i
        create_file_and_write(os.path.join(temp_dir, 'expert_exp.json'), json.dumps(expert_exps, indent=4, ensure_ascii=False))
        logger.info(f">>> The retrieved expert experiences are saved in: {os.path.join(temp_dir, 'expert_exp.json')}")

        hl_response = None
        if self.HL_enable == True:
            hl_response = self._HL_response(temp_dir, code, run_response, expert_exps)

        response = FeedbackResponse(
            run_response=run_response,
            syntax_response=syntax_response,
            hl_response=hl_response
        )
        create_file_and_write(os.path.join(temp_dir, 'user_content.txt'), json.dumps(response.to_prompt(), indent=4, ensure_ascii=False))
        logger.info(f">>> The user content for the next iteration is saved in: {os.path.join(temp_dir, 'user_content.txt')}")
    
        return response
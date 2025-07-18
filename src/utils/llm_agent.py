from openai import OpenAI
import time
import os
import json

import logging

logger = logging.getLogger(__name__)

class AgentBase():
    """
    Base class for all LLM agents.
    """
    def __init__(self, model="qwen-max-latest", use_stream=False, use_local=False, system_prompt="你是精通网络设备和网络运维的专家。", history_k=10, timeout=20, verbose=False):    
        """
        Initialize the agent with the specified model and platform.
        Args:
            model (str): The name of the model to use. Defaults to "qwen-max-latest".
            platform (str): The platform to use. Defaults to "dashscope".
            stream (bool): Whether to use stream mode. Defaults to False.
            use_local (bool): Whether to use the local API. Defaults to False.
            role (str): The role of the assistant. 
            history_k (int): The number of messages to keep in the history. Defaults to 10.
        """
        # system_prompt_backup = "You are a very helpful assistant with great expertise in network operations and maintenance."
        self.model_stream_mode = {
            "qwen-max-latest": False,
            "deepseek-v3": False,
            "deepseek-r1": True,
            "gpt-4o": False,
            "o1-2024-12-17": True
        }
        self.model_platform = {
            "qwen-max-latest": "dashscope",
            "deepseek-v3": "dashscope",
            "deepseek-r1": "dashscope",
            "gpt-4o": "openai",
            "o1-2024-12-17": "openai"
        }
        self.use_stream = use_stream or self.model_stream_mode[model]
        self.name = "AgentBase"
        self.use_local = use_local
        self.model = model
        self.platform = self.model_platform[model]
        self.history_k = history_k
        self.timeout = timeout  # seconds
        self.verbose = verbose
        if self.use_local:
            openai_api_key = "EMPTY"
            openai_api_base = "http://localhost:8000/v1"
            self.client = OpenAI(
                api_key=openai_api_key,
                base_url=openai_api_base,
            )
        elif self.platform == "openai":
            self.client = OpenAI()
        elif self.platform == "dashscope":
            self.client = OpenAI(
                api_key=os.getenv("DASHSCOPE_API_KEY"), 
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            )
        elif self.platform == "deepseek":
            self.client = OpenAI(
                api_key = os.getenv("DEEPSEEK_API_KEY"),
                base_url = "https://api.deepseek.com/v1",
                timeout = 30
            )
        else:
            raise ValueError("Invalid platform")
        logger.info(f"AgentBase init: {self.platform} {self.model}")
        self.history = [{"role": "system", "content":  system_prompt}]
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def response(self, prompt):
        self.history.append({"role": "user", "content": prompt})
        if self.verbose:
            logger.info(f"{self.name} history before API call: {self.history} (len: {len(str(self.history))})")

        # Ensure that history has the correct format for messages
        for message in self.history:
            if not isinstance(message, dict) or "role" not in message or "content" not in message:
                raise ValueError("Invalid history format: every message must be a dictionary with 'role' and 'content' fields.")
        
        # Make API call
        completion = None
        logger.info(f"Calling API...")
        while completion is None:
            try:
                if self.use_stream:
                    completion = self.client.chat.completions.create(
                        model=self.model,
                        messages=self.history,
                        stream=True,
                        stream_options={"include_usage": True}
                    )
                else:
                    completion = self.client.chat.completions.create(
                        model=self.model,
                        messages=self.history,
                        stream=False
                    )
            except Exception as e:
                logger.error(f"Error: {e}")
                time.sleep(2)
                continue

            if self.use_stream:

                reasoning_content = ""
                answer_content = ""
                result = ""
                is_answering = False   # 判断是否结束思考过程并开始回复
                for chunk in completion:
                    # 如果chunk.choices为空，则打印usage
                    if not chunk.choices:
                        logger.info("\nUsage:")
                        logger.info(chunk.usage)
                    else:
                        delta = chunk.choices[0].delta
                        # 打印思考过程
                        if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
                            # logger.info(delta.reasoning_content)
                            print(delta.reasoning_content, end='', flush=True)
                            reasoning_content += delta.reasoning_content
                        else:
                            # 开始回复
                            if delta.content != "" and is_answering == False:
                                logger.info("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
                                is_answering = True
                            # 打印回复过程
                            # logger.info(delta.content)
                            print(delta.content, end='', flush=True)
                            if delta.content:
                                answer_content += delta.content
                result = answer_content
            else:
                if not completion:
                    logger.error("No completion returned. Maybe LLM timeout.")
                    time.sleep(2)
                    continue
                self.prompt_tokens += completion.usage.prompt_tokens
                self.completion_tokens += completion.usage.completion_tokens
                result = completion.choices[0].message.content
                logger.info(f"{self.name} response: {result}")

        logger.info(f"API call completed")
        self.history.append({"role": "assistant", "content": result})
        if len(self.history) > self.history_k:
            self.history = [self.history[0]] + self.history[-self.history_k:]
        return result
    
    def clear_context(self):
        self.history = [{"role": "system", "content": "You are a network operation and maintenance expert."}]

    def run(self, query="Hello, how are you?"):
        return self.response(query)


if  __name__ == "__main__":
    # Set logger parameters, output to command line
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    agent = AgentBase(model='deepseek-r1', verbose=True, system_prompt="You are a helpful assistant.")
    print(agent.run("How to understand RFC by LLM?"))
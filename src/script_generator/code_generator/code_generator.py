import logging, json
from .task import Task
from ..feedback import FeedbackAgent
from ..llm_client import LLMClinet
from ..retriever import APIRetriever, APIDocEntry, ExampleRetriever, ExampleEntry

logger = logging.getLogger(__name__)

class CodeGenerator:
    def __init__(self,
                 llm_client: LLMClinet,
                 api_retriever: APIRetriever,
                 example_retriever: ExampleRetriever,
                 feedback_agent: FeedbackAgent,
                ):
        assert llm_client.registered() == True
        self.llm_client: LLMClinet = llm_client
        self.api_retriever = api_retriever
        self.example_retriever = example_retriever
        self.feedback_agent = feedback_agent

    def gen_init_message(self, system_prompt: str, task: Task):
        self.llm_client.clear_messages()
        # System prompt
        self.llm_client.append_message('system', system_prompt)

        # Retrieve relevant examples based on task description
        examples: list[ExampleEntry] = self.example_retriever.retrieve(task.to_example_query())
        logger.debug(f"The following are the retrieved example codes:\n")
        logger.debug(f"{json.dumps([example.example.task['prompt'] for example in examples], indent=4, ensure_ascii=False)}\n")
        self.llm_client.append_message('user', self.example_retriever.to_prompt(examples))

        # Retrieve relevant APIs based on task description
        retrieved_apis: list[APIDocEntry] = self.api_retriever.retrieve(task.to_api_query(), examples=examples)
        logger.debug(f"The following are the retrieved APIs:")
        logger.debug(f"{json.dumps({api.method_name: api.description for api in retrieved_apis}, indent=4, ensure_ascii=False)}\n\n")
        self.llm_client.append_message('user', self.api_retriever.to_prompt(retrieved_apis))

        # Task description
        self.llm_client.append_message('user', task.to_prompt())

    def step(self, user_content: str | None = None, assistant_content: str | None = None):
        if assistant_content is not None: self.llm_client.append_message('assistant', assistant_content)
        if user_content is not None: self.llm_client.append_message('user', user_content)
        response = self.llm_client.request()
        logger.debug(f'>>> CodeGenerator.step():\n\t- assistant_content: {assistant_content}\n\t- user_content: {user_content}\n\t- LLM response: {response}')
        return response

    # TODO: Additionally, LLM may also generate some explanatory text, which may also be valuable and should be extracted
    def _get_code_from_response(self, code: str):
        start_marker = "```python"
        end_marker = "```"
        start_pos = code.find(start_marker)
        end_pos = code.rfind(end_marker)
        if start_pos == -1 or end_pos == -1: return code
        if start_pos >= end_pos: return code
        start_pos += len(start_marker)
        substring = code[start_pos:end_pos]
        return substring

    def run(self,
            system_prompt: str,
            task: Task,
            max_iter: int = 10,
            remove_past_assistant: bool = False,
            assistant_content: str | None = None,
            user_content: str | None = None
        ):

        self.gen_init_message(system_prompt=system_prompt, task=task)
        logger.debug(f'>>> Init message: {json.dumps(self.llm_client.get_messages(), ensure_ascii=False, indent=4)}')

        result_code = None
        codes: list[str] = []
        responses: list[str] = []
        for iter in range(max_iter):
            logger.info(f"\n\n==================================== CodeGenerator.run(): iter = {iter + 1} Begin ========================================" )
            if remove_past_assistant == True:
                self.llm_client.clear_messages_by_role('assistant')
                logger.info('>>> Clear past assistent content')

            # Interact with LLM to generate code
            logger.info(f">>> CodeGenerator.step(): new user_content = {user_content}")
            logger.info('>>> Generating Code')
            llm_response = self.step(user_content=user_content, assistant_content=assistant_content)
            code = self._get_code_from_response(llm_response)
            codes.append(code)

            # Send to feedback model for execution
            logger.info(">>> Sending request(code, cfg, tesdtbed) to feedback agent")
            response = self.feedback_agent.request(code, task.dir)
            responses.append(response.response)
            logger.debug(f">>> Response from feedback agent: {json.dumps(response.response, indent=4, ensure_ascii=False)}\n")

            if response.success() == True:
                result_code = code
                break
            
            # Get the content for the next round to feed to LLM
            assistant_content = llm_response
            user_content = response.to_prompt()
            logger.info(f"==================================== CodeGenerator.run(): iter = {iter + 1} End ========================================\n\n\n")

        if result_code is None:
            logger.error(f">>> The code can not be generated in {max_iter} iter(s)\n")
        return result_code, codes, responses
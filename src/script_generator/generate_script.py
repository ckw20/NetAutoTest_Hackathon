import logging, os
from .retriever import APIRetriever, ExampleRetriever, ExperienceRetriever, RetrieverConfig
from .code_generator import CodeGenerator
from .llm_client import LLMClinet
from .feedback import FeedbackAgent
from .common import load_json
from .code_generator.task import load_task, load_examples

logger = logging.getLogger(__name__)

def generate_script(cfg: dict, run_script_api: callable):
    logger.info("\nCreating LLM Client")
    llm_client = LLMClinet()
    llm_client.register_online(
        api_key=cfg["Code"]["Generator"]["api_key"],
        base_url=cfg["Code"]["Generator"]["base_url"],
        model=cfg["Code"]["Generator"]["model"]
    )

    logger.info("\nCreating API Retriever")
    api_retriever = APIRetriever(
        api_doc=load_json(cfg["API"]["doc"]),
        spec_apis=cfg["API"]["specified"],
        retriever_config=RetrieverConfig(cfg["API"]["Retriever"])
    )

    logger.info("\nLoading Tasks")
    task = load_task(
        cfg["Task"]["dir"],
        cfg["Task"]["task"]
    )
    logger.debug(f"\ntask prompt:\n{task.to_prompt()}\n")

    logger.info("\nCreating Example Retriever")
    examples = load_examples(cfg["Example"]["dir"])
    if "dir_no_cfg" in cfg["Example"].keys():
        examples += load_examples(cfg["Example"]["dir_no_cfg"], no_cfg=True)
    example_retriever = ExampleRetriever(
        examples=examples,
        spec_examples=cfg["Example"]["specified"],
        retriever_config=RetrieverConfig(cfg["Example"]["Retriever"])
    )

    logger.info("\nLoading Experience Retriever")
    experience_retriever = ExperienceRetriever(
        exp_pool_path=cfg["Experience"]["pool_path"],
        retriever_config=RetrieverConfig(cfg["Experience"]["Retriever"])
    )

    logger.info("\nCreating Feedback Agent")
    script_path = f"./temp_script/{cfg['current_time']}"
    feedback_agent = FeedbackAgent(
        request_api=run_script_api,
        script_path=script_path,
        experience_retriever=experience_retriever,
        HL_enable=cfg["Feedback"]["HL_enable"]
    )

    logger.info("\nCreating Code Generator")
    code_generator = CodeGenerator(
        llm_client=llm_client,
        api_retriever=api_retriever,
        example_retriever=example_retriever,
        feedback_agent=feedback_agent
    )


    system_prompt = cfg["Code"]["system_prompt"]
    if os.path.exists(system_prompt):
        system_prompt = open(system_prompt, "r").read()
    logger.debug(f"system_prompt: {system_prompt}\n")

    assistant_content = cfg["Code"]["assistant_content"]
    user_content = cfg["Code"]["user_content"]
    if assistant_content is not None: assert user_content is not None,\
        "When assistant_content is provided, user_content must also be provided."
    if assistant_content is not None: assistant_content = open(assistant_content, "r").read()
    if user_content is not None: user_content = open(user_content, "r").read()

    logger.info("\nStart code_generator.run()")
    result_code, history_codes, responses = code_generator.run(
        system_prompt=system_prompt,
        task=task,
        max_iter=cfg["Code"]["max_iter"],
        remove_past_assistant=cfg["Code"]["remove_past_assistant"],
        assistant_content=assistant_content,
        user_content=user_content
    )
    logger.debug(f"\nresult code: {result_code}\n")
    return result_code, history_codes, responses

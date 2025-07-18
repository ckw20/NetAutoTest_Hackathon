import logging, json, random
from math import ceil
from .retriever import APIRetriever, ExampleEntry
from ..code_generator.task import load_examples, load_json
from ..common import create_file_and_write


logger = logging.getLogger(__name__)

def prepare_positive_dataset(cfg: dict):
    dataset_cfg = cfg['Finetune']['dataset_positive']
    if dataset_cfg['generate']['enable']:
        api_retriever = APIRetriever(
            api_doc=load_json(cfg["API"]["doc"]),
            model_type=None,
            model_name_or_path=None
        )

        examples = load_examples(cfg["Example"]["dir"])
        if "dir_no_cfg" in cfg["Example"].keys():
            examples += load_examples(cfg["Example"]["dir_no_cfg"], no_cfg=True)
        examples = [ExampleEntry(example) for example in examples]

        removed_api = [
            "shutdown_tester",
            "tabulate"
        ]
        dataset: list[dict] = []
        for example in examples:
            api_names = example.extract_api(module='TesterLibrary.base')
            spec_apis = [api for api in api_names if api not in removed_api]
            apis = api_retriever.load_spec_apis(spec_apis)
            dataset.append({
                "query": example.corpus(),
                "apis": [api.to_dict_prompt() for api in apis]
            })
        path = dataset_cfg['generate']['save_path']
        create_file_and_write(path, json.dumps(dataset, indent=4, ensure_ascii=False))
    else:
        assert dataset_cfg['load']['enable'] == True
        dataset = load_json(dataset_cfg['load']['path'])

    return dataset

def generate_negative_dataset(cfg: dict, dataset_positive_size: int):
    dataset_cfg = cfg['Finetune']['dataset_negative']
    if dataset_cfg['enable'] == False: return []
    size = ceil(dataset_positive_size * dataset_cfg['ratio'])
    api_retriever = APIRetriever(
        api_doc=load_json(cfg["API"]["doc"]),
        model_type=None,
        model_name_or_path=None
    )
    examples = load_examples(cfg["Example"]["dir"])
    if "dir_no_cfg" in cfg["Example"].keys():
        examples += load_examples(cfg["Example"]["dir_no_cfg"], no_cfg=True)
    examples = [ExampleEntry(example) for example in examples]

    random.seed(dataset_cfg['seed'])
    apis = random.choices(api_retriever.entries, k=size)
    examples = random.choices(examples, k=size)
    dataset: list[dict] = []
    for api, example in zip(apis, examples):
        dataset.append({
            'query': example.corpus(),
            'apis': [api.to_dict_prompt()]
        })
    return dataset

def finetune(dataset):
    pass

def evaluate():
    pass
import logging, datetime, os, json, torch
from collections import defaultdict
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainingArguments, SentenceTransformerTrainer
from src.utils.logger import configure_root_logger
from src.script_generator.common import args2cfg, parse_args
import src.script_generator as sg
from datasets import load_dataset, Dataset, concatenate_datasets
from sentence_transformers.losses import MultipleNegativesRankingLoss, CoSENTLoss
from sentence_transformers.training_args import BatchSamplers
from sentence_transformers.evaluation import InformationRetrievalEvaluator

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

def load_my_dataset(cfg):
    dataset_positive = sg.fintune.prepare_positive_dataset(cfg)
    dataset_positive_size = sum([len(data['apis']) for data in dataset_positive])
    dataset_negative = sg.fintune.generate_negative_dataset(cfg, dataset_positive_size)
    dataset_negative_size = sum([len(data['apis']) for data in dataset_negative])
    logger.info(f'dataset_positive size: {dataset_positive_size}, dataset_negative size: {dataset_negative_size}')
    """
        Fromat of above dataset: [{'query': str, 'apis': [{...}]}]
        For more details for format of the dict in apis, see
        src.script_generator.retriever.entry.APIDocEntry.to_dict_prompt()
    """

    # TODO: Improve me
    def query_to_anchor(query: str):
        return query
    # TODO: Improve me
    def api_to_corpus(api: dict):
        return api['method_name'] + ': ' + api['description']

    def fit_datasets_Dataset_format(dataset: list[dict], label: int):
        assert label in [0, 1]
        dataset_new = []
        for data in dataset:
            anchor = query_to_anchor(data['query'])
            for api in data['apis']:
                dataset_new.append((
                    anchor, api_to_corpus(api)
                ))
        dict_list = [{"anchor": anchor, "corpus": corpus, "label": label} for anchor, corpus in dataset_new]
        return Dataset.from_list(dict_list)

    dataset_positive = fit_datasets_Dataset_format(dataset_positive, 1)
    dataset_negative = fit_datasets_Dataset_format(dataset_negative, 0)

    dataset = concatenate_datasets([dataset_positive, dataset_negative])
    logger.debug(f'dataset: {dataset}')
    """
    dataset: Dataset({features: ['anchor', 'corpus', 'label']})
    """
    return dataset

def load_model(cfg: dict) -> SentenceTransformer:
    model_cfg = cfg['Finetune']['model']
    # TODO: Add CrossEncoder (perhaps in another file...)
    assert model_cfg['type'] == 'SentenceTransformer', 'Currently only support SentenceTransformer'
    if model_cfg['type'] == 'SentenceTransformer':
        model = SentenceTransformer(model_cfg['name_or_path'], device=device)
    return model

def load_evaluator(dataset: Dataset, name: str = "") -> InformationRetrievalEvaluator:
    positive_pairs = dataset.filter(lambda example: example['label'] == 1)
    queries, qid, tot_qid = {}, {}, 0  # {qid: query}, {query: qid}
    corpuses, cid, tot_cid = {}, {}, 0  # {cid: corpus}, {corpus: cid}
    relevant_docs = defaultdict(set)  # {qid: set(cid)}

    for example in positive_pairs:
        query = example['anchor']
        corpus = example['corpus']
        if query not in qid.keys():
            tot_qid += 1
            qid[query] = f'q_{tot_qid}'
        if corpus not in cid.keys():
            tot_cid += 1
            cid[corpus] = f'c_{tot_cid}'
        queries[qid[query]] = query
        corpuses[cid[corpus]] = corpus
        relevant_docs[qid[query]].add(cid[corpus])
    relevant_docs = dict(relevant_docs)

    # print(tot_qid, tot_cid)
    # for q_id in relevant_docs.keys():
    #     print(queries[q_id])
    #     result = []
    #     for c_id in relevant_docs[q_id]:
    #         result.append(corpuses[c_id].split(':')[0])
    #     print(sorted(result), len(result))

    evaluator = InformationRetrievalEvaluator(
        queries=queries,
        corpus=corpuses,
        relevant_docs=relevant_docs,
        name=name,
        accuracy_at_k=[100], # Accuracy here is meaningless
        precision_recall_at_k=[5, 10, 15, 20, 25, 30, 40, 50], # Precision here is meaningless
        map_at_k=[5, 10, 15, 20, 25, 30, 40, 50]
    )

    return evaluator

if __name__ == '__main__':
    args = parse_args()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    cfg: dict = args2cfg(args, current_time)
    if not os.path.exists("logs"): os.mkdir("logs")
    LOG_LEVELS = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARNING": logging.WARNING, "ERROR": logging.ERROR, "CRITICAL": logging.CRITICAL}
    configure_root_logger(
        filename=f"logs/fintune_{current_time}.log", level=LOG_LEVELS[args.log_level],
        format_str="[%(asctime)s] %(name)-25s %(levelname)-8s %(message)s" if args.verbose else "%(message)s"
    )
    logger = logging.getLogger(__name__)

    # Load dataset and split
    dataset = load_my_dataset(cfg)
    train_test = dataset.train_test_split(test_size=0.2, shuffle=True, seed=42)
    train_dataset, test_dataset = train_test['train'], train_test['test']

    # Load evaluator
    test_evaluator = load_evaluator(test_dataset, 'test-evaluator')
    all_evaluator = load_evaluator(dataset, 'all-evaluator')

    # Load model and loss
    model = load_model(cfg) # TODO: Choose better base model

    # TODO: Choose better loss function
    if len(dataset) == sum(dataset['label']):
        train_dataset = train_dataset.select_columns(['anchor', 'corpus'])
        test_dataset = test_dataset.select_columns(['anchor', 'corpus'])
        loss = MultipleNegativesRankingLoss(model)
    else:
        loss = CoSENTLoss(model)

    # TODO: Find better args
    output_dir = os.path.join(cfg['Finetune']['model']['output_path'],f"{cfg['Finetune']['model']['output_name']}_{current_time}")
    args = SentenceTransformerTrainingArguments(
        # Required parameter:
        output_dir=output_dir,
        # Optional training parameters:
        num_train_epochs=500,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-6,
        warmup_ratio=0.1,
        fp16=False,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=False,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,  # losses that use "in-batch negatives" benefit from no duplicates
        # Optional tracking/debugging parameters:
        eval_strategy="steps",
        eval_steps=10,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2,
        logging_steps=100,
        run_name=f"{cfg['Finetune']['model']['output_name']}_{current_time}",  # Will be used in W&B if `wandb` is installed
    )

    # Evaluate before train
    all_evaluator(model)

    # Train
    trainer = SentenceTransformerTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        loss=loss,
        evaluator=test_evaluator, # perhaps we'd better use test_evaluator
    )
    trainer.train()

    # Evaluate after train
    all_evaluator(model)
    test_evaluator(model)

    # Save the trained model
    model.save_pretrained(os.path.join(output_dir, 'final'))

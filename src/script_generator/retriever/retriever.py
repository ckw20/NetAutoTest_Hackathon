from abc import ABC, abstractmethod
import json, os
import numpy as np
from typing import Literal
import bm25s, jieba, torch, logging
from .entry import Entry, APIDocEntry, ExampleEntry, ExperienceEntry
from ..common import load_json, create_file_and_write
from ..llm_client import LLMClinet
from sentence_transformers import SentenceTransformer, CrossEncoder

logger = logging.getLogger(__name__)

class LocalRetriever:
    def __init__(self,
                 model_type: Literal["SentenceTransformer", "CrossEncoder"] = "SentenceTransformer",
                 model_name_or_path: str = "multi-qa-mpnet-base-cos-v1"
                ):
        self.model_type = model_type
        self.model = None
        try:
            assert self.model_type in ["SentenceTransformer", "CrossEncoder"], 'self.model_type in ["SentenceTransformer", "CrossEncoder"]'
            if self.model_type == "SentenceTransformer":
                self.model = SentenceTransformer(model_name_or_path, device=torch.device("cuda"))
                assert next(self.model.parameters()).is_cuda
            elif self.model_type == "CrossEncoder":
                self.model = CrossEncoder(model_name_or_path, device=torch.device("cuda"))
                assert next(self.model.model.parameters()).is_cuda
        except Exception as e:
            logger.debug(f"Error in Retrieve.__init__(): {e}")
        self.model: SentenceTransformer | CrossEncoder = self.model

        self.entries: list[Entry] = []
        self.stopwords = None

    def corpus(self):
        return [entry.corpus() for entry in self.entries]

    def BM25(self, query: str, corpus: list[str], k: int = 300) -> list[int]:
        splitter = lambda desc: jieba.lcut(desc, cut_all=False, HMM=True, use_paddle=False)
        tokenizer = bm25s.tokenization.Tokenizer(lower=True, splitter=splitter, stopwords=self.stopwords, stemmer=None)
        corpus_tokens = tokenizer.tokenize(corpus)
        query_tokens = tokenizer.tokenize([query])
        retriever = bm25s.BM25()
        retriever.index(corpus_tokens)
        results, scores = retriever.retrieve(query_tokens, k=k)
        logger.debug(f"BM25 scores: {scores}")
        # results is in (n_queries, k) shape
        return [results[0, i] for i in range(results.shape[1])]

    def rank(self, query: str, corpus: list[str], k: int):
        if self.model_type == "SentenceTransformer":
            corpus_emb = self.model.encode(corpus)
            query_emb = self.model.encode(query)
            scores = torch.squeeze(self.model.similarity(corpus_emb, query_emb))
            scores, ids = torch.topk(scores, k)
        elif self.model_type == "CrossEncoder":
            ranks = self.model.rank(query, corpus)[0: k]
            scores = [rank['score'] for rank in ranks]
            ids = [rank['corpus_id'] for rank in ranks]
        return scores, ids

    def retrieve(self,
                 query: str,
                 k: int = 100,
                 BM25_enable: bool = False,
                 BM25_k: int = 1000
                ):
        corpus = self.corpus()
        entries = self.entries
        if BM25_enable == True:
            BM25_id = self.BM25(query, corpus, k=BM25_k)
            corpus = [corpus[id] for id in BM25_id]
            entries = [entries[id] for id in BM25_id]
        scores, ids = self.rank(query, corpus, k)
        # logger.debug(f"Retrieve scores: {scores}")
        # logger.debug(f"Retrieve ids: {ids}")
        return [entries[id] for id in ids]

class RemoteRetriever:
    def __init__(self,
                 base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1",
                 api_key: str = "Your API Key",
                 embedding_model: str | None = "text-embedding-v3",
                 rerank_model: str | None = "gte-rerank-v2",
                 corpus2embedding_path: str | None = None
            ):
        self.embedding_client = None
        if embedding_model is not None:
            self.embedding_client = LLMClinet()
            self.embedding_client.register_online(api_key=api_key, base_url=base_url, model=embedding_model)
        self.rerank_client = None
        if rerank_model is not None:
            self.rerank_client = LLMClinet()
            self.rerank_client.register_online(api_key=api_key, base_url=base_url, model=rerank_model)
        self.entries: list[Entry] = []
        self.embeddings: list[list[float]] = []
        self.corpus2embedding_path = corpus2embedding_path
        self.corpus2embedding: dict[str, list[float]] = {}
        if corpus2embedding_path is not None:
            if not os.path.exists(corpus2embedding_path):
                create_file_and_write(corpus2embedding_path, "{}")
            try:
                self.corpus2embedding = load_json(corpus2embedding_path)
            except Exception as e:
                logger.error(f"Error in RemoteRetriever.__init__(): {e}")
                logger.error(f"Failed to load corpus2embedding from {corpus2embedding_path}, initializing with empty dict.")
                self.corpus2embedding = {}
        self.entries: list[Entry] = []

    def corpus(self):
        return [entry.corpus() for entry in self.entries]

    def add_entry(self, entry: Entry):
        self.entries.append(entry)
        if self.embedding_client is not None:
            embedding = self.corpus2embedding.get(entry.corpus(), None)
            if embedding is None:
                embedding = self.embedding_client.embedding(entry.corpus())
                embedding = (embedding / np.linalg.norm(embedding)).tolist()  # Normalize the embedding
            self.embeddings.append(embedding)
            self.corpus2embedding[entry.corpus()] = embedding
            self.save_corpus2embedding()

    def save_corpus2embedding(self, path: str | None = None):
        if path is None: path = self.corpus2embedding_path
        if path is not None:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(self.corpus2embedding, ensure_ascii=False, indent=4))

    def retrieve_from_embedding(self, query: str, k: int = 100):
        query_embedding = self.embedding_client.embedding(query)
        query_embedding = query_embedding / np.linalg.norm(query_embedding)  # Normalize the embedding
        scores = [np.dot(embedding, query_embedding) for embedding in self.embeddings]
        ids = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.entries[id] for id in ids]

    def rerank(self, query: str, entries: list[Entry], top_n: int = 10):
        documents = [entry.corpus() for entry in entries]
        reranked_results = self.rerank_client.rerank(query, documents, top_n)
        ids = sorted(range(len(reranked_results)), key=lambda i: reranked_results[i]['relevance_score'], reverse=True)[:top_n]
        return [entries[reranked_results[id]['index']] for id in ids]

    def retrieve(self, query: str, embedding_k: int = 100, rerank_k: int = 10):
        if len(self.entries) == 0: return []
        assert self.embedding_client is not None or self.rerank_client is not None, \
            "At least one of embedding_client or rerank_client must be set."
        results = self.entries
        if self.embedding_client is not None:
            results = self.retrieve_from_embedding(query, embedding_k)
        if self.rerank_client is not None:
            results = self.rerank(query, results, rerank_k)
        return results

class RetrieverConfig:
    def __init__(self, cfg: dict):
        self.local_model_type: Literal["SentenceTransformer", "CrossEncoder"] | None = cfg.get("local_model_type", None)
        self.local_model_name_or_path: str | None = cfg.get("local_model_name_or_path", None)
        self.remote_base_url: str | None = cfg.get("remote_base_url", None)
        self.remote_api_key: str | None = cfg.get("remote_api_key", None)
        self.remote_embedding_model: str | None = cfg.get("remote_embedding_model", None)
        self.remote_rerank_model: str | None = cfg.get("remote_rerank_model", None)
        self.remote_corpus2embedding_path: str | None = cfg.get("remote_corpus2embedding_path", None)

        self.local_embedding_k: int = cfg.get("local_embedding_k", None)
        self.local_BM25_enable: bool = cfg.get("local_BM25_enable", False)
        self.local_BM25_k: int = cfg.get("local_BM25_k", None)
        self.remote_embedding_k: int = cfg.get("remote_embedding_k", None)
        self.remote_rerank_k: int = cfg.get("remote_rerank_k", None)

class Retriever(ABC):
    def __init__(
        self,
        retriever_config: RetrieverConfig | None = None,
    ):
        # load retriever config
        self.retriever_config: RetrieverConfig = retriever_config
        local_model_type = retriever_config.local_model_type
        local_model_name_or_path = retriever_config.local_model_name_or_path
        remote_base_url = retriever_config.remote_base_url
        remote_api_key = retriever_config.remote_api_key
        remote_embedding_model = retriever_config.remote_embedding_model
        remote_rerank_model = retriever_config.remote_rerank_model
        remote_corpus2embedding_path = retriever_config.remote_corpus2embedding_path

        # initialize retriever
        self.local_retriever: LocalRetriever | None = None
        self.remote_retriever: RemoteRetriever | None = None
        self.entries: list[Entry] = []
        if local_model_name_or_path is not None and local_model_type is not None:
            logger.info(f"Initializing LocalRetriever with model_type={local_model_type}, model_name_or_path={local_model_name_or_path}")
            self.local_retriever = LocalRetriever(local_model_type, local_model_name_or_path)
        if remote_base_url is not None and remote_api_key is not None:
            logger.info(f"Initializing RemoteRetriever with base_url={remote_base_url}, api_key={remote_api_key}, "
                        f"embedding_model={remote_embedding_model}, rerank_model={remote_rerank_model}, " \
                        f"corpus2embedding_path={remote_corpus2embedding_path}")
            self.remote_retriever = RemoteRetriever(
                base_url=remote_base_url,
                api_key=remote_api_key,
                embedding_model=remote_embedding_model,
                rerank_model=remote_rerank_model,
                corpus2embedding_path=remote_corpus2embedding_path
            )
        assert self.local_retriever is not None or self.remote_retriever is not None, \
            "At least one of local_retriever or remote_retriever must be set."

    # should be called after entries are set
    def _sync_entries(self):
        if self.local_retriever is not None:
            self.local_retriever.entries = self.entries
        if self.remote_retriever is not None:
            for entry in self.entries:
                self.remote_retriever.add_entry(entry)

    def retrieve(
        self,
        query: str
    ):
        # load retrieve config
        local_k = self.retriever_config.local_embedding_k
        local_BM25_enable = self.retriever_config.local_BM25_enable
        local_BM25_k = self.retriever_config.local_BM25_k
        remote_embedding_k = self.retriever_config.remote_embedding_k
        remote_rerank_k = self.retriever_config.remote_rerank_k

        # retrieve results
        results: list[Entry] = []
        if self.local_retriever is not None:
            results += self.local_retriever.retrieve(query, local_k, local_BM25_enable, local_BM25_k)
        if self.remote_retriever is not None:
            results += self.remote_retriever.retrieve(query, embedding_k=remote_embedding_k, rerank_k=remote_rerank_k)
        results = list({entry.corpus(): entry for entry in results}.values())
        return results

class APIRetriever(Retriever):
    def __init__(self,
                 api_doc: dict, # json
                 spec_apis: str | None = None,
                 retriever_config: RetrieverConfig | None = None
                ):
        super().__init__(retriever_config)
        self.api_doc = api_doc
        self.entries: list[APIDocEntry] = list(filter(lambda item: item.type == "func", [APIDocEntry(item) for item in self.api_doc]))
        self._sync_entries()
        logger.info(f"info: {len(self.entries)} api loaded from api doc.")
        self.stopwords = ["的", "。", "和", ",", " ", "测试", "仪表", "流量", "发送", "接收", "功能"]
        self.specified_api: list[APIDocEntry] = self.load_spec_apis(load_json(spec_apis) if spec_apis is not None else None)

    def load_spec_apis(self, api_names: list[str]):
        if api_names is None: return []
        specified_api = []
        for api_name in api_names:
            specified_api_entry: list[APIDocEntry] = []
            for api_entry in self.entries:
                if api_entry.method_name == api_name or api_entry.method_name.endswith('.' + api_name):
                    specified_api_entry.append(api_entry)
            if len(specified_api_entry) == 0:
                logger.debug(f"Error in APIRetriever.__init__(): No API named {api_name}")
            elif len(specified_api_entry) > 1:
                logger.debug(f"Error in APIRetriever.__init__(): Duplicate API named {api_name}")
            else: specified_api.append(specified_api_entry[0])
        return specified_api

    def merge_api(self, dst_api: list[APIDocEntry], src_api: list[APIDocEntry], k: int = -1):
        dst_api_name = [api.method_name for api in dst_api] \
                     + [api.method_name.split('.')[-1] for api in dst_api if '.' in api.method_name]
        filtered_src_api = list(filter(lambda api: api.method_name not in dst_api_name, src_api))
        merged_api = dst_api + filtered_src_api
        return merged_api[0: k] if k >= 0 else merged_api

    def extract_api_from_example(self, examples: list[ExampleEntry], module='TesterLibrary.base', k: int = -1):
        extracted_api: list[APIDocEntry] = []
        for example in examples:
            api_names = example.extract_api(module)
            extracted_api = self.merge_api(extracted_api, self.load_spec_apis(api_names), k)
        return extracted_api

    def retrieve(self, query: str, examples: list[ExampleEntry] | None = None):
        apis = self.specified_api
        extracted_api = self.extract_api_from_example(examples)
        apis = self.merge_api(apis, extracted_api)
        retrieved_api: list[APIDocEntry] = super().retrieve(query)
        return self.merge_api(apis, retrieved_api)[0: len(retrieved_api)]

    def to_prompt(self, apis: list[APIDocEntry]):
        prompt = "The following is a list of APIs that may be used, provided in JSON format as a list, each item describing an API you may use. The format and meaning of each field are as follows:\n"
        template = json.dumps({
                "method_name": "The name of the API, which you can use directly after 'from TesterLibrary.base import *'",
                "description": "Description of the function of this API",
                "parameters": [{
                    "parameter_name": "Parameter name",
                    "parameter_type": "Parameter type",
                    "description": "Parameter description",
                    "default": "Default value of the parameter, if there is no default value, it will be filled as null",
                    "range_or_options": "Parameter value range or optional values, if none, it will be filled as null"
                }],
                "return": "Description of the return value",
                "return_type": "Type of the return value"
            }, indent=4, ensure_ascii=False
        )
        prompt = "The following is a list of APIs that may be used: \n"
        prompt += template + "\n"
        prompt += json.dumps([api.to_dict_prompt() for api in apis], ensure_ascii=False) + "\n"
        # logger.debug(f"Retrieved APIs:\n{json.dumps([api.to_dict_prompt() for api in apis], ensure_ascii=False, indent=4)}")
        prompt += "The above is the description of the APIs that may be used."
        return prompt

class ExampleRetriever(Retriever):
    def __init__(self,
                 examples,
                 spec_examples: str | None = None,
                 retriever_config: RetrieverConfig | None = None
                ):
        super().__init__(retriever_config)
        self.entries: list[ExampleEntry] = [ExampleEntry(example) for example in examples]
        self._sync_entries()
        self.specified_example: list[ExampleEntry] = self.load_spec_examples(load_json(spec_examples) if spec_examples is not None else None)

    def load_spec_examples(self, spec_tc_nos: str | None = None):
        # Load specified Examples
        if spec_tc_nos is None: return []
        specified_example = []
        for specified_tc_no in spec_tc_nos:
            specified_example_entry: list[ExampleEntry] = []
            for example_entry in self.entries:
                if example_entry.example.tc_no == specified_tc_no:
                    specified_example_entry.append(example_entry)
            if len(specified_example_entry) == 0:
                logger.debug(f"Error in ExampleRetriever.__init__(): No Example which tc_no is {specified_tc_no}")
            elif len(specified_example_entry) > 1:
                logger.debug(f"Error in ExampleRetriever.__init__(): No Example which tc_no is {specified_tc_no}")
            else: specified_example.append(specified_example_entry[0])
        return specified_example

    def retrieve(self, query):
        specified_example_tc_no = [example.example.tc_no for example in self.specified_example]
        retrieve_example: list[ExampleEntry] = super().retrieve(query)
        # logger.debug(f"ExampleRetriever.retrieve(): {len(retrieve_example)} examples retrieved")
        # for example in retrieve_example:
        #     logger.debug(f"ExampleRetriever.retrieve(): Retrieved example: {example.example.tc_no}")
        retrieve_example = list(filter(lambda example: example.example.tc_no not in specified_example_tc_no, retrieve_example))
        return (self.specified_example + retrieve_example)[0: len(retrieve_example)]

    def to_prompt(self, examples: list[ExampleEntry]):
        prompt = "The following are example codes that may be used.\n"
        for example in examples:
            prompt += example.to_prompt() + "\n"
        prompt += "The above are example codes that may be used."
        return prompt

class ExperienceRetriever(Retriever):
    def __init__(self,
                 exp_pool_path: str,
                 retriever_config: RetrieverConfig | None = None
                ):
        super().__init__(retriever_config)
        self.exp_pool_path = exp_pool_path
        if not os.path.exists(exp_pool_path):
            create_file_and_write(exp_pool_path, "[]")
        try:
            experiences: list[dict] = load_json(exp_pool_path)
        except Exception as e:
            logger.error(f"Error in ExperienceRetriever.__init__(): {e}")
            logger.error(f"Failed to load experiences from {exp_pool_path}, initializing with empty list.")
            experiences = []
        self.entries: list[ExperienceEntry] = [ExperienceEntry(experience) for experience in experiences]
        self._sync_entries()

    def retrieve(self, query: dict) -> list[ExperienceEntry]:
        return super().retrieve(ExperienceEntry(query).corpus())

    def add_experience(self, experience: dict):
        entry = ExperienceEntry(experience)
        assert entry.suggestion is not None, "ExperienceEntry.suggestion to be stored must be set."
        self.entries.append(entry)
        if self.remote_retriever is not None:
            self.remote_retriever.add_entry(entry)
        self.save_experience(self.exp_pool_path)

    def save_experience(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps([entry.to_dict() for entry in self.entries], ensure_ascii=False, indent=4))
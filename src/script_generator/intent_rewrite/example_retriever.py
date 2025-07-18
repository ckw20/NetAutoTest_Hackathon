import numpy as np
import requests
import Levenshtein
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from sklearn.metrics.pairwise import cosine_similarity
from example_builder import clean_text


class ExampleRetriever:
    def __init__(self, examples, config):
        self.examples = examples
        self.config = config
        self.language = config.get("language", "zh")

        # 清洗所有意图
        if self.language == "en":
            self.cleaned_intents = [clean_text(e.intent_en) for e in examples]
            self.intent_texts = [e.intent_en for e in examples]
        else:
            self.cleaned_intents = [clean_text(e.intent) for e in examples]
            self.intent_texts = [e.intent for e in examples]


        retriever_cfg = config["retriever"]
        self.use_local = retriever_cfg.get("use_local", True)
        self.use_remote = retriever_cfg.get("use_remote", False)
        self.use_rerank = retriever_cfg.get("use_rerank", False)

        if self.use_local:
            self.model = SentenceTransformer(retriever_cfg["local_model"])
            self.intent_vectors = self.model.encode(self.cleaned_intents, convert_to_numpy=True)
            self.bm25 = BM25Okapi([text.split() for text in self.cleaned_intents])
        if self.use_rerank:
            self.reranker = CrossEncoder(retriever_cfg["rerank_model"])
    

    def get_intent(self, example):
        """根据语言返回中文或英文 intent"""
        return example.intent_en if self.language == "en" else example.intent

    def retrieve(self, query_intent: str, top_k: int = 5):
        cleaned_query = clean_text(query_intent)

        scores = []

        if self.use_local:
            query_vec = self.model.encode([cleaned_query], convert_to_numpy=True)
            emb_scores = cosine_similarity(query_vec, self.intent_vectors)[0]
            bm25_scores = self.bm25.get_scores(cleaned_query.split())
            edit_scores = np.array([Levenshtein.ratio(cleaned_query, ci) for ci in self.cleaned_intents])

            def norm(x):
                return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-8)

            emb_norm = norm(emb_scores)
            bm25_norm = norm(np.array(bm25_scores))
            edit_norm = edit_scores

            combined = 0.5 * emb_norm + 0.3 * bm25_norm + 0.2 * edit_norm
            scores = list(enumerate(combined))

        elif self.use_remote:
            payload = {
                "query": cleaned_query,
                "corpus": self.cleaned_intents,
                "top_k": top_k
            }
            headers = {"Authorization": f"Bearer {self.config['retriever']['remote_api_key']}"}
            resp = requests.post(self.config["retriever"]["remote_base_url"], json=payload, headers=headers)
            scores = list(enumerate(resp.json()["scores"]))

        top_indices = sorted(scores, key=lambda x: -x[1])[:top_k]
        top_examples = [(self.examples[i], float(score)) for i, score in top_indices]

        if self.use_rerank:
            pairs = [(cleaned_query, clean_text(self.get_intent(ex))) for ex, _ in top_examples]
            rerank_scores = self.reranker.predict(pairs)

            def softmax(x):
                x = np.array(x)
                e_x = np.exp(x - np.max(x))
                return e_x / (e_x.sum() + 1e-8)

            rerank_scores = softmax(rerank_scores)

            fused = []
            for (ex, orig_score), rerank_score in zip(top_examples, rerank_scores):
                final_score = 0.6 * orig_score + 0.4 * rerank_score
                fused.append((ex, final_score))

            top_examples = sorted(fused, key=lambda x: -x[1])

        return top_examples

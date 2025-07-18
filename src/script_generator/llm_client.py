import logging, dashscope
from dashscope.api_entities.dashscope_response import ReRankResponse
from typing import Iterable, Literal
from openai import OpenAI
from openai.types.create_embedding_response import CreateEmbeddingResponse

logger = logging.getLogger(__name__)

class LLMClinet:
    def __init__(self):
        self.type = "Not Registered"
        self.client: OpenAI = None
        self.model: str = None
        self.messages: list[dict] = []

    def register_online(self,
                        api_key: str = "Your API Key", # sk-208810d2a9cf48b1aab8ac749cc2e767
                        base_url: str = "https://api.deepseek.com",
                        model: str = "deepseek-chat" # deepseek-chat for V3 and deepseek-reasoner for R1
                    ):
        self.type = "Online"
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        # self.max_tokens = self.get_model_max_tokens()
        # logger.info(f"Model {model} registered successfully with max tokens: {self.max_tokens}")

    # TODO: fix bug in it
    def get_model_max_tokens(self, model: str | None = None):
        if model is None: model = self.model
        try:
            model_info = self.client.models.retrieve(model)
            max_tokens = model_info.max_tokens
        except Exception as e:
            logger.error(f"Failed to retrieve model info for {model}: {e}. Set max_tokens to 0.")
            max_tokens = 0
        return max_tokens

    # check if the model supports chat completions
    def validate_model(self, model: str | None = None):
        if model is None: model = self.model
        try:
            self.client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": "Test message"}],
                stream=False
            )
        except Exception as e:
            logger.error(f"Model {model} does not support chat completions: {e}")
            raise ValueError(f"Model {model} does not support chat completions. Please use a different model.")

    def register_offline(self, model: str):
        raise NotImplementedError("Local LLM Client registration is not implemented yet.")

    def append_message(self, role: Literal["system", "user", "assistant"], content: str):
        assert role in ["system", "user", "assistant"], "Role must be 'system', 'user' or 'assistant'."
        self.messages.append({"role": role, "content": content})

    def append_messages(self, messages: Iterable[dict]):
        for message in messages:
            assert "role" in message and "content" in message, "Each message must contain 'role' and 'content'."
            self.append_message(message["role"], message["content"])

    def clear_messages(self):
        self.messages = []

    def clear_messages_by_role(self, role: Literal["system", "user", "assistant"] | Iterable[str] | None = None):
        if role is None: self.messages = []
        else:
            if isinstance(role, str): role = [role]
            assert all(r in ["system", "user", "assistant"] for r in role), "Role must be 'system', 'user' or 'assistant'."
            self.messages = [msg for msg in self.messages if msg["role"] not in role]

    def clear_messages_by_index(self, indices: int | Iterable[int] | None = None):
        if indices is None: self.messages = []
        else:
            if isinstance(indices, int): indices = [indices]
            assert all(isinstance(i, int) for i in indices), f"Indices must be integers."
            indices = [i if i >= 0 else len(self.messages) + i for i in indices]
            assert all(0 <= i < len(self.messages) for i in indices), f"Indices must be within the range of messages."
            self.messages = [msg for i, msg in enumerate(self.messages) if i not in indices]

    def get_messages(self):
        return self.messages

    def request(self, messages: list[dict] | None = None):
        if messages is None: messages = self.messages
        assert len(messages) > 0, "Messages cannot be empty. Please set messages before requesting."

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=False
        )
        return response.choices[0].message.content

    def embedding(self, input: str, dimensions: int = 1024, encoding_format: str = "float"):
        embedding: CreateEmbeddingResponse = self.client.embeddings.create(
            model=self.model, # e.g. text-embedding-v3
            input=input,
            dimensions=dimensions,
            encoding_format=encoding_format
        )
        return embedding.data[0].embedding

    def rerank(self, query, documents: list[str], top_n: int = 10):
        response: ReRankResponse = dashscope.TextReRank.call(
            model=self.model,
            query=query,
            documents=documents,
            top_n=top_n,
            return_documents=True,
            api_key=self.client.api_key
        )
        return response.output.results # list of {'index': int, 'relevance_score': float, 'document': {'text': str}}

    def registered(self):
        if self.type == "Not Registered":
            return False
        return True

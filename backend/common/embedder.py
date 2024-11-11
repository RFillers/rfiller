import openai
from common.constants import EMBEDDER_MODEL_NAME, OPENAI_API_KEY


class Embedder:
    open_ai_client: openai.OpenAI
    model_name: str

    def __init__(self, embedding_model_name: str = EMBEDDER_MODEL_NAME) -> None:
        self.open_ai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.model_name = embedding_model_name

    def embed(self, text_list: list[str]) -> list[list[float]]:
        embedded_values = self.open_ai_client.embeddings.create(
            input=text_list, model=self.model_name, dimensions=512
        ).data

        return [embedded_value.embedding for embedded_value in embedded_values]

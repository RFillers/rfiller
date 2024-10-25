from qdrant_client import QdrantClient
from backend.embedder.embedder import Embedder


class ApiGlobalVariables:
    """Global variables for the API."""

    qdrant_client: QdrantClient
    embedder: Embedder


api_global_variables = ApiGlobalVariables()

from qdrant_client import QdrantClient


class ApiGlobalVariables:
    """Global variables for the API."""

    qdrant_client: QdrantClient


api_global_variables = ApiGlobalVariables()

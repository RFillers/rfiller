from qdrant_client import QdrantClient
from common.embedder import Embedder
from supabase import Client


class ApiGlobalVariables:
    """Global variables for the API."""

    qdrant_client: QdrantClient
    embedder: Embedder
    supabase_client: Client


api_global_variables = ApiGlobalVariables()

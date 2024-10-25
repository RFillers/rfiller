from fastapi import FastAPI, HTTPException, Request
from supabase import create_client, Client
from qdrant_client import QdrantClient
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from backend.embedder.embedder import Embedder
from common.api_global_variables import api_global_variables
from common.constants import QDRANT_HOST, QDRANT_PORT


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Load clients when the app starts.

    FastAPI doc about lifespan events: https://fastapi.tiangolo.com/advanced/events/.
    """
    api_global_variables.qdrant_client = QdrantClient(
        host=QDRANT_HOST, port=QDRANT_PORT
    )
    api_global_variables.embedder = Embedder()

    yield

    api_global_variables.qdrant_client.close()


app = FastAPI(lifespan=lifespan)

# Supabase configuration
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Qdrant configuration
qdrant_client = QdrantClient("localhost", port=6333)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI + Supabase + Qdrant app"}


# Define more endpoints to handle Supabase and Qdrant operations here


@app.post("/add-vector/")
async def add_vector(request: Request):
    data = await request.json()
    vector = data.get("vector")
    payload = data.get("payload")
    if vector:
        qdrant_client.upsert(
            collection_name="your_collection",
            points=[{"id": "unique-id", "vector": vector, "payload": payload}],
        )
        return {"message": "Vector added successfully"}
    raise HTTPException(status_code=400, detail="Vector data missing")


@app.post("/search/")
async def search_vector(request: Request):
    data = await request.json()
    query_vector = data.get("vector")
    if query_vector:
        result = qdrant_client.search(
            collection_name="your_collection", query_vector=query_vector, limit=5
        )
        return result
    raise HTTPException(status_code=400, detail="Query vector missing")

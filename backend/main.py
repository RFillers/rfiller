from fastapi import FastAPI, HTTPException, Request
from supabase import create_client
from qdrant_client import QdrantClient
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from common.embedder import Embedder
from common.api_global_variables import api_global_variables
from common.constants import QDRANT_HOST, QDRANT_PORT, SUPABASE_URL, SUPABASE_KEY


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Load clients when the app starts.

    FastAPI doc about lifespan events: https://fastapi.tiangolo.com/advanced/events/.
    """
    api_global_variables.qdrant_client = QdrantClient(
        host=QDRANT_HOST, port=QDRANT_PORT
    )
    api_global_variables.embedder = Embedder()
    if SUPABASE_URL and SUPABASE_KEY:
        api_global_variables.supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
    else:
        raise ValueError("Supabase URL or Key missing")

    yield

    api_global_variables.qdrant_client.close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def read_root():
    return {"message": "Welcome to the FastAPI + Supabase + Qdrant app"}


@app.post("/embedding")
async def embbed_file(request: Request):
    data = await request.json()
    vector = data.get("vector")
    payload = data.get("payload")
    if vector:
        api_global_variables.qdrant_client.upsert(
            collection_name="your_collection",
            points=[{"id": "unique-id", "vector": vector, "payload": payload}],
        )
        return {"message": "Vector added successfully"}
    raise HTTPException(status_code=400, detail="Vector data missing")


@app.post("/search")
async def search_vector(request: Request):
    data = await request.json()
    query_vector = data.get("vector")
    if query_vector:
        result = api_global_variables.qdrant_client.search(
            collection_name="your_collection", query_vector=query_vector, limit=5
        )
        return result
    raise HTTPException(status_code=400, detail="Query vector missing")


@app.get("/message")
async def get_messages():
    try:
        response = (
            api_global_variables.supabase_client.table("message").select("*").execute()
        )
    except Exception:
        raise HTTPException(status_code=404, detail="Item not found")

    return response.data

from fastapi import Depends, FastAPI, HTTPException, Request
from qdrant_client import QdrantClient
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from common.dependencies import get_db
from common.embedder import Embedder
from common.api_global_variables import api_global_variables
from common.constants import QDRANT_HOST, QDRANT_PORT
from database.models import User
from database.db import engine, Base

from sqlalchemy.orm import Session


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Load clients when the app starts.

    FastAPI doc about lifespan events: https://fastapi.tiangolo.com/advanced/events/.
    """

    Base.metadata.create_all(bind=engine)

    api_global_variables.qdrant_client = QdrantClient(
        host=QDRANT_HOST, port=QDRANT_PORT
    )
    api_global_variables.embedder = Embedder()

    yield

    api_global_variables.qdrant_client.close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def read_root():
    return {"message": "Welcome to the FastAPI + PostgreSQL + Qdrant app"}


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


@app.get("/user")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

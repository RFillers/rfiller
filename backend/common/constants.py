import os

from dotenv import load_dotenv

load_dotenv()

# Qdrant config
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
QDRANT_EMBEDDING_SIZE = 512
QDRANT_THEMES_REVIEWS_ASSOCIATION_SCORE_TRESHOLD = 0.5
MAX_AMOUNT_OF_REVIEWS_TO_ASSOCIATE_TO_THEME = 200

# Embedder config
EMBEDDER_MODEL_NAME = "text-embedding-3-small"

# OpenAI config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Supabase config
SUPABASE_URL = os.getenv("DATABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")

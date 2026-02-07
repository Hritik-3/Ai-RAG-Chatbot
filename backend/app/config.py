import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

COLLECTION_NAME = "rulebook"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Loads .env
# Reads your keys safely
# Defines:
# which Qdrant collection to use
# which embedding model to use
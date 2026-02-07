from sentence_transformers import SentenceTransformer
from app.retrieval.qdrant_client import client
from app.config import COLLECTION_NAME

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def retrieve_context(question, limit=3):
    q_vec = model.encode(question).tolist()
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=q_vec,
        limit=limit
    )
    return "\n".join([h.payload["text"] for h in hits])



# Convert question to embedding vector
# Search Qdrant for similar embeddings.
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from app.config import COLLECTION_NAME, QDRANT_URL, QDRANT_API_KEY
import uuid

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def store_chunks(chunks):
    vectors = model.encode([c["text"] for c in chunks])
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={"size": len(vectors[0]), "distance": "Cosine"}
    )
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            {
                "id": str(uuid.uuid4()),
                "vector": vectors[i].tolist(),
                "payload": chunks[i]
            } for i in range(len(chunks))
        ]
    )


    
# This is the MOST IMPORTANT ingestion file.
# It does:
# ✅ create embeddings
# ✅ store in qdrant
from app.ingestion.load_rulebook import load_rulebook
from app.ingestion.chunker import make_chunks
from app.ingestion.embed_and_store import store_chunks

data = load_rulebook("data/rulebook.jsonl")
chunks = make_chunks(data)
store_chunks(chunks)

print("Ingestion complete")


# ✅ Reads rulebook
# ✅ Creates chunks
# ✅ Embeds chunks
# ✅ Saves vectors in Qdrant cloud


# ✅ Step 1: run ingestion
# python scripts/ingest_once.py

# ✅ Step 2: user asks a question
# Frontend → /chat

# ✅ Step 3: chatbot logic
# embed question
# search Qdrant
# get best rule chunks

# ✅ Step 4: OpenAI
# receives: context + question
# answers using rulebook
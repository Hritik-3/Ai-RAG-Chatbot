from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="RAG Rulebook Chatbot")

app.include_router(chat_router, prefix="/chat")

# (App Entry Point)
# We create FastAPI server (app = FastAPI())
# We connect chat routes (/chat)
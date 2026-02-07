# 

from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.retrieval.retriever import retrieve_context
from app.llm.openai_client import ask_llm

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest):
    context = retrieve_context(req.question)
    answer = ask_llm(req.question, context)
    return ChatResponse(answer=answer)


# When user sends question:
# retrieve_context(question)
# → gets relevant rules from Qdrant
# ask_llm(question, context)
# → OpenAI gives final answer based on context
# So this file connects everything.
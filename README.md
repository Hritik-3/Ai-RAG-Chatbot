# AI-Powered RAG Chatbot Backend

A **Retrieval-Augmented Generation (RAG)** based chatbot backend that answers domain-specific questions using a vector database and Large Language Model (LLM) integration.

This system combines **semantic search** with **LLM reasoning** to provide context-aware responses grounded in custom knowledge documents.

---

## 🚀 Tech Stack

- **Backend Framework:** FastAPI  
- **Language Model:** OpenAI GPT models  
- **Embeddings:** Sentence Transformers  
- **Vector Database:** Qdrant  
- **Language:** Python  
- **Architecture:** RESTful API + RAG Pipeline  

---

## 🧠 How It Works (RAG Pipeline)

1. Documents are loaded from the knowledge base  
2. Text is split into chunks  
3. Chunks are converted into embeddings  
4. Embeddings are stored in Qdrant  
5. User query is embedded  
6. Relevant chunks are retrieved  
7. Retrieved context is sent to the LLM  
8. LLM generates a grounded answer  

---

## 📁 Project Structure


# 🤖 AI RAG Chatbot

A powerful Retrieval-Augmented Generation (RAG) chatbot built with FastAPI, OpenAI, and Qdrant vector database. This chatbot intelligently retrieves relevant information from your documents and generates accurate, context-aware responses.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-red.svg)

## ✨ Features

- **Retrieval-Augmented Generation (RAG)**: Combines the power of semantic search with LLM generation
- **Vector Database**: Uses Qdrant for efficient similarity search
- **OpenAI Integration**: Leverages OpenAI's language models for intelligent responses
- **FastAPI Backend**: High-performance, modern API framework
- **RESTful API**: Easy-to-use endpoints for chat interactions
- **Document Processing**: Automatically processes and indexes documents for retrieval
- **Real-time Responses**: Fast query processing and response generation

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Git**: [Install Git](https://git-scm.com/downloads)
- **OpenAI API Key**: [Get API Key](https://platform.openai.com/api-keys)

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hritik-3/Ai-RAG-Chatbot.git
cd Ai-RAG-Chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

Alternatively, use a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Set up the required environment variables:

#### On macOS/Linux:
```bash
export OPENAI_API_KEY=your_openai_api_key
export QDRANT_HOST=localhost
export QDRANT_PORT=6333
```

#### On Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_openai_api_key
set QDRANT_HOST=localhost
set QDRANT_PORT=6333
```

#### On Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_openai_api_key"
$env:QDRANT_HOST="localhost"
$env:QDRANT_PORT="6333"
```

### Alternative: Using .env File

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

## 🚀 Running the Project

### 1️⃣ Start Qdrant Vector Database

```bash
docker run -p 6333:6333 qdrant/qdrant
```

This will start the Qdrant vector database on `http://localhost:6333`

### 2️⃣ Start the FastAPI Backend

```bash
uvicorn backend.app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### 3️⃣ Access the Application

- **Interactive API Documentation**: http://127.0.0.1:8000/docs
- **Alternative API Docs**: http://127.0.0.1:8000/redoc
- **API Base URL**: http://127.0.0.1:8000

## 📚 API Documentation

### Chat Endpoint

**POST** `/chat`

Send a question to the chatbot and receive an AI-generated response.

#### Request Body:
```json
{
  "question": "What rules apply to inventory approval?"
}
```

#### Response:
```json
{
  "answer": "Based on the retrieved context...",
  "sources": ["document1.pdf", "document2.pdf"],
  "confidence": 0.95
}
```

### Example cURL Request:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"question": "What rules apply to inventory approval?"}'
```

### Example Python Request:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"question": "What rules apply to inventory approval?"}
)

print(response.json())
```

## 📁 Project Structure

```
Ai-RAG-Chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── models.py            # Pydantic models
│   │   ├── services/
│   │   │   ├── rag_service.py   # RAG implementation
│   │   │   ├── vector_store.py  # Qdrant integration
│   │   │   └── llm_service.py   # OpenAI integration
│   │   └── utils/
│   │       └── document_processor.py
│   └── requirements.txt         # Python dependencies
│
├── data/                        # Document storage
├── tests/                       # Unit tests
├── .env.example                 # Example environment variables
├── .gitignore
├── README.md
└── LICENSE
```

## 🧪 Usage Examples

### Adding Documents

```python
# Example: Adding documents to the vector database
from backend.app.services.document_processor import process_documents

process_documents("path/to/your/documents")
```

### Querying the Chatbot

```python
import requests

# Ask a question
response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"question": "Explain the company's return policy"}
)

print(response.json()["answer"])
```

## 🛠️ Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
# Install black
pip install black

# Format code
black backend/
```

### Linting

```bash
# Install flake8
pip install flake8

# Run linter
flake8 backend/
```

## 🐳 Docker Deployment (Optional)

```bash
# Build the Docker image
docker build -t ai-rag-chatbot .

# Run the container
docker run -p 8000:8000 --env-file .env ai-rag-chatbot
```

## 🔍 Troubleshooting

### Common Issues

**1. Port already in use**
```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

**2. Qdrant connection error**
- Ensure Docker is running
- Verify Qdrant container is running: `docker ps`

**3. OpenAI API key error**
- Verify your API key is correct
- Check if environment variable is set: `echo $OPENAI_API_KEY`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hritik**
- GitHub: [@Hritik-3](https://github.com/Hritik-3)

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for the language models
- [Qdrant](https://qdrant.tech/) for the vector database
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- All contributors who help improve this project

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Contact the maintainer through GitHub

---

⭐ **Star this repository if you find it helpful!**

# LLM + RAG-Based Function Execution API

## 📌 Project Overview

This project is a FastAPI-based automation API that utilizes LLM (Large Language Model) + RAG (Retrieval-Augmented Generation) to dynamically retrieve and execute predefined system automation functions. Users can send natural language prompts, and the system intelligently maps them to corresponding automation functions, generating and executing Python code in real-time.

## ✨ Features

Dynamic Function Retrieval: Uses ChromaDB as a vector store to match user prompts with predefined automation functions.

AI-Powered Function Execution: LLM processes natural language inputs and generates executable Python code for the mapped function.

FastAPI-based REST API: Provides a robust and scalable API with well-defined endpoints for automation task execution.

##🚀 API Endpoints

1️⃣ Execute Automation Function

Endpoint: POST /execute

Request Body:

{ "prompt": "Open Chrome browser" }

Response:

{
  "function": "open_chrome",
  "code": "from automation_functions import open_chrome\n\ndef main():\n    try:\n        open_chrome()\n        print(\"Execution successful.\")\n    except Exception as e:\n        print(f\"Error executing function: {e}\")\n\nif __name__ == \"__main__\":\n    main()",
  "output": null
}

## 🛠️ Setup & Installation

1. Clone the Repository

git clone https://github.com/your-repo/llm-rag-function-api.git
cd llm-rag-function-api

2. Install Dependencies

pip install -r requirements.txt

3. Run the API Server

uvicorn app:app --host 127.0.0.1 --port 8000

## 🔧 Technologies Used

FastAPI (for API development)

FAISS / ChromaDB (for vector search and function retrieval)

Hugging Face Transformers (for embedding generation and LLM inference)

Python OS & Webbrowser Modules (for executing system automation tasks)

## 🔥 Future Enhancements

Add support for custom user-defined functions.

Implement session-based memory for context-aware automation.

Integrate logging and monitoring for function execution tracking.

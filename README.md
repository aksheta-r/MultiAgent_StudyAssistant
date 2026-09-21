# Multi-Agent AI Study Assistant

An intelligent RAG-based learning workspace that uses specialized AI agents for document-grounded explanations, summaries, and quiz generation.

## Overview

The Multi-Agent AI Study Assistant is an academic learning application that allows students to upload a PDF document and interact with its content through multiple specialized AI agents.

The system combines Retrieval-Augmented Generation (RAG), vector embeddings, a vector database, and task-specific AI agents to generate responses grounded in the uploaded academic material.

## Features

- Upload academic PDF documents
- Retrieve relevant information from uploaded documents
- Explain academic topics using an Explainer Agent
- Generate chapter summaries and key points
- Generate quizzes with MCQs and short-answer questions
- Route requests to the appropriate specialized agent
- Evaluate and improve generated responses
- Interactive Streamlit interface

## System Architecture


Academic PDF
     |
     v
PDF Processing
     |
     v
Text Splitting and Chunking
     |
     v
Hugging Face Embeddings
     |
     v
ChromaDB
     |
     v
Relevant Content Retrieval
     |
     v
Router Agent
   /    |    \
  /     |     \
 v      v      v
Explainer Summary Quiz
 Agent    Agent  Agent
   \       |      /
    \      |     /
     v     v    v
      Evaluator Agent
             |
             v
       Final Response


## How It Works

### 1. Document Upload

The user uploads an academic PDF through the Streamlit interface.

### 2. Document Processing

The PDF is loaded using PyPDF and divided into smaller text chunks using recursive text splitting.

### 3. Embedding Generation

The text chunks are converted into vector representations using the `all-MiniLM-L6-v2` Hugging Face embedding model.

### 4. Vector Storage

The generated embeddings are stored in ChromaDB to support similarity-based retrieval.

### 5. Relevant Content Retrieval

When the user selects a learning task, the system retrieves relevant sections from the uploaded document based on the user's query.

### 6. Task Routing

The Router Agent identifies the selected learning task and routes the request to the appropriate specialized agent.

### 7. Specialized Agent Processing

The system currently includes three task-specific agents:

- **Explainer Agent** - explains concepts clearly, breaks down key ideas, and provides examples.
- **Summary Agent** - generates chapter summaries, key points, and important definitions.
- **Quiz Agent** - generates MCQs, short-answer questions, and answers.

### 8. Response Evaluation

The generated response is passed to the Evaluator Agent, which improves its formatting, clarity, and readability before displaying the final response.


## AI Agents

| Agent | Responsibility |

| Router Agent | Routes the selected learning task to the appropriate agent |
| Explainer Agent | Explains concepts clearly, breaks down key ideas, and provides examples |
| Summary Agent | Generates chapter summaries, key points, and important definitions |
| Quiz Agent | Generates MCQs, short-answer questions, and answers |
| Evaluator Agent | Improves the clarity, formatting, and readability of the generated response |

## Technologies Usedx
- Python
- Streamlit
- LangChain
- Google Gemini
- ChromaDB
- Hugging Face Embeddings
- Sentence Transformers
- PyPDF
- Retrieval-Augmented Generation (RAG)

## Project Structure
MultiAgent_StudyAssistant
|
├── agents.py       # AI agents for explanation, summary, quiz, and evaluation
├── app.py          # Streamlit application and user interface
├── rag.py          # PDF processing, chunking, embeddings, and vector database
├── router.py       # Routes tasks to specialized agents
├── style.css       # Custom Streamlit styling
├── temp.pdf        # Sample academic document
├── requirements.txt
├── .gitignore
└── README.md

## Getting Started

1. Clone the Repository
git clone https://github.com/aksheta-r/MultiAgent_StudyAssistant.git
cd MultiAgent_StudyAssistant
2. Create a Virtual Environment
python -m venv venv
For Windows:
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure the Gemini API Key
Set your Google Gemini API key as an environment variable.
For Windows PowerShell:
$env:GOOGLE_API_KEY="your_api_key_here"
Do not place API keys directly inside the source code.
5. Run the Application
streamlit run app.py

Example Workflow
Upload Academic PDF
        |
        v
Select a Learning Task
        |
        v
Retrieve Relevant Content
        |
        v
Router Agent
        |
        +----> Explainer Agent
        |
        +----> Summary Agent
        |
        +----> Quiz Agent
                    |
                    v
             Evaluator Agent
                    |
                    v
             Final Response

The same workflow can be used for explanation, summary generation, and quiz generation.


## Security
API credentials are stored using environment variables rather than hard-coded in source files.
The generated ChromaDB vector database is created during document processing and is not included in the repository.

## Future Enhancements
Conversation memory for multi-turn learning
Support for multiple uploaded documents
Improved agent coordination
Personalized study plans
Progress tracking
Additional quiz formats
Cloud deployment

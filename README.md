
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

The application follows a document-grounded multi-agent workflow:

1. The user uploads an academic PDF.
2. The PDF is processed and divided into smaller text chunks.
3. Text chunks are converted into vector embeddings.
4. The embeddings are stored in ChromaDB.
5. Relevant content is retrieved based on the user's request.
6. The Router Agent identifies the required learning task.
7. The request is passed to the appropriate specialized agent.
8. The generated response is passed through the Evaluator Agent.
9. The final response is displayed through the Streamlit interface.

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

- Explainer Agent - explains concepts clearly, breaks down key ideas, and provides examples.
- Summary Agent - generates chapter summaries, key points, and important definitions.
- Quiz Agent - generates MCQs, short-answer questions, and answers.

### 8. Response Evaluation

The generated response is passed to the Evaluator Agent, which improves its formatting, clarity, and readability before displaying the final response.

## AI Agents

### Router Agent

Routes the selected learning task to the appropriate specialized agent.

### Explainer Agent

Uses retrieved document context to explain topics, break down key concepts, provide simple examples, and highlight important notes.

### Summary Agent

Generates chapter summaries, key points, and important definitions from the retrieved document content.

### Quiz Agent

Generates three multiple-choice questions, two short-answer questions, and their answers from the retrieved content.

### Evaluator Agent

Improves the formatting, clarity, and readability of the generated response.

## Technologies Used

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

```text
MultiAgent_StudyAssistant/
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
````

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aksheta-r/MultiAgent_StudyAssistant.git
cd MultiAgent_StudyAssistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Set your Google Gemini API key as an environment variable.

For Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

Do not place API keys directly inside the source code.

### 5. Run the Application

```bash
streamlit run app.py
```

## Example Workflow

A typical learning workflow is:

```text
Upload Academic PDF
        |
        v
Select Learning Task
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
```

The same workflow can be used for explanation, summary generation, and quiz generation.

## Security

API credentials are stored using environment variables rather than hard-coded in source files.

The generated ChromaDB vector database is created during document processing and is not included in the repository.

## Future Enhancements

* Conversation memory for multi-turn learning
* Support for multiple uploaded documents
* Improved agent coordination
* Personalized study plans
* Progress tracking
* Additional quiz formats
* Cloud deployment

## Project

Multi-Agent AI Study Assistant

Built using Python, LangChain, RAG, Gemini, ChromaDB, Hugging Face Embeddings, and Streamlit.

````


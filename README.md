# Mini Document Q\&A API:


A Retrieval-Augmented Generation (RAG) system built with FastAPI. The application answers questions from a PDF document using FAISS for semantic search and Groq as the Large Language Model (LLM).



## Development Note:

This project was implemented in approximately "7 hours", including project setup, PDF processing, embedding generation, FAISS indexing, RAG pipeline implementation, FastAPI integration, testing, and documentation.



## Features:

- Load and process PDF documents

- Split text into chunks

- Generate embeddings using Sentence Transformers

- Store embeddings in a FAISS vector index

- Retrieve the most relevant chunks

- Generate answers using Groq

- Return both the answer and source page numbers



## Project Structure:


Mini\_Document\_Q\&A/

│

├── data/

│   └── NexaFlow\_S200\_Manual.pdf

│

├── pdf\_processing.py

├── pdf\_path.py

├── vector\_store.py

├── llm.py

├── rag.py

├── api.py

│

├── requirements.txt

├── Task Report.docx

├── .env

├── .env.example

├── .gitignore

└── README.md


## Requirements:

Before running the project, make sure you have:

- Python 3.10 or later
- Git
- A Groq API Key
- Internet connection (required for embedding model download and Groq API)



## Setup:


### 1. Clone the repository

-> bash:

git clone https://github.com/mahmoudhussein77/RAG-Task.git

cd RAG-Task




### 2. Create a virtual environment


-> Windows:

-> bash:


python -m venv venv

venv\\Scripts\\activate



-> Linux / macOS

-> bash:


python3 -m venv venv

source venv/bin/activate




### 3. Install dependencies


-> bash:

pip install -r requirements.txt



### 4. Create a `.env` file


Add your Groq API key:


-> .env:

GROQ_API_KEY=your_api_key_here



### 5. Add pdf path to pdf_path.py:

pdf_source = your_pdf_path



### 6. Running the API


Start the FastAPI server:

-> bash:

uvicorn api:app --reload


-> The API will be available at: http://127.0.0.1:8000

-> Swagger documentation: http://127.0.0.1:8000/docs




## API Example:


### POST `/ask`


Request:


```json

{
   "question": "What is the operating pressure?"

}

```


Response:


```json

{

   "answer": "The typical operating pressure is 10 to 14 bar.",

   "sources": {"page": 1}, {"page": 2},

   "found": true

}

```




## Technologies Used:


- Python

- FastAPI

- FAISS

- Sentence Transformers

- PyMuPDF (fitz)

- Groq API


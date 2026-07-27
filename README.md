\# Mini Document Q\&A API



A Retrieval-Augmented Generation (RAG) system built with FastAPI. The application answers questions from a PDF document using FAISS for semantic search and Groq as the Large Language Model (LLM).





\## Features



\- Load and process PDF documents

\- Split text into chunks

\- Generate embeddings using Sentence Transformers

\- Store embeddings in a FAISS vector index

\- Retrieve the most relevant chunks

\- Generate answers using Groq

\- Return both the answer and source page numbers





\## Project Structure



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

```







\## Setup



\### 1. Clone the repository



\-> bash:



git clone <repository\_url>

cd D:\\Mini\_Document\_Q\&A







\### 2. Create a virtual environment



\-> Windows:

\-> bash:



python -m venv venv

venv\\Scripts\\activate

```



\-> Linux / macOS

\-> bash:



python3 -m venv venv

source venv/bin/activate

```





\### 3. Install dependencies



\-> bash:



pip install -r requirements.txt

```





\### 4. Create a `.env` file



Add your Groq API key:



```env

GROQ\_API\_KEY=your\_api\_key\_here

```



\### 5. Add pdf path to pdf\_path.py





\### 6. Running the API



Start the FastAPI server:



\-> bash:

uvicorn api:app --reload





\-> The API will be available at: http://127.0.0.1:8000



\-> Swagger documentation: http://127.0.0.1:8000/docs



\---





\## API Example



\### POST `/ask`



Request:



```json

{

&#x20;   "question": "What is the operating pressure?"

}

```



Response:



```json

{

&#x20;   "answer": "The typical operating pressure is 10 to 14 bar.",

&#x20;   "sources": {"page": 1}, {"page": 2},

&#x20;   "found": true

}

```



\---





\## Technologies Used



\- Python

\- FastAPI

\- FAISS

\- Sentence Transformers

\- PyMuPDF (fitz)

\- Groq API


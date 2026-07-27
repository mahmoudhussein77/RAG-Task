from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question


app = FastAPI()


class Question(BaseModel):
    question: str



@app.get("/")
def home():

    return {
        "message": "Mini Document Q&A API is running"
    }



@app.post("/ask")
def ask(data: Question):

    return ask_question(data.question)
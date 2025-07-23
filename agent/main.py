# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from Flow_chain import get_rag_chain

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/CH")
async def ask_question(query: QueryRequest):
    result = get_rag_chain(query.question)


    # return {
    #     "question": query.question,
    #     "answer": result["result"],  # <- the generated answer
    #     "sources": [doc.metadata for doc in result["source_documents"]]
    # }
###################################this file is used and both return are working above 

    return result

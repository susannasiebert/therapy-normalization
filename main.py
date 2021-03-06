"""Main application for FastAPI"""
from therapy.query import normalize
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Endpoint that returns default example of API root endpoint"""
    return {"Hello": "World"}


@app.get("/query/{q_string}")
def read_query(q_string: str):
    """Endpoint to return normalized responses for a the query"""
    resp = normalize(q_string)
    return resp

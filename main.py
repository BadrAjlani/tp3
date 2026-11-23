
"""FastAPI application providing basic mathematical operations."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """Return the home message."""
    return {"message": "Hello, World!"}


@app.get("/addition")
def addition(a: int, b: int):
    """Calculate the sum of two integers."""
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.get("/greeting")
def greeting(name: str):
    """Return a personalized greeting."""
    return {
        "message": f"Hello {name}, welcome to the application!"
    }


@app.get("/soustraction")
def soustraction(a: int, b: int):
    """Calculate the difference between two integers."""
    return {"result a-b=": a - b, "developer": "Dev1"}

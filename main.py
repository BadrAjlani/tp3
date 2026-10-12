
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello {name}, welcome to the application!"
    }
    
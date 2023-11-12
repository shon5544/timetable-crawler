from fastapi import FastAPI

app = FastAPI()

@app.get("/login")
def login():
    return "It's a Good Day"
from fastapi import FastAPI
from src.auth.routes import router as auth_router

app = FastAPI(title="FastAPI + MongoDB Example")

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB is working 🚀"}

from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="MediReport AI")

@app.get("/")
def root():
    return {"status": "MediReport AI backend running"}


app.include_router(health.router)
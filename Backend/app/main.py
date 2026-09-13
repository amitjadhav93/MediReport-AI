from fastapi import FastAPI

app = FastAPI(title="MediReport AI")

@app.get("/")
def root():
    return {"status": "MediReport AI backend running"}
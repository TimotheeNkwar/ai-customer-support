from fastapi import FastAPI

app = FastAPI(title="A FastAPI application")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
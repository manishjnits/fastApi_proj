from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI(title="FaslaAPI Project")


@app.get("/")
async def read_root():
    return {"message": "Welcome to FaslaAPI Project"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

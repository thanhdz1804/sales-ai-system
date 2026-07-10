from fastapi import FastAPI

app = FastAPI(
    title="Sales AI System API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Sales AI System API is running"
    }

from fastapi import FastAPI
from app.core.database import Base, engine

import app.models.role
import app.models.user

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sales AI System API is running"}

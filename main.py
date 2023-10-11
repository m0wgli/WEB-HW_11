from fastapi import FastAPI, Path, Query, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Hello from REST API CONTACTS"}
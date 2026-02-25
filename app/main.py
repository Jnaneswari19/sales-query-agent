from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal
from . import models, schemas
from .llm_sql import run_nl_query

app = FastAPI(title="Sales Query Agent")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tables")
def list_tables():
    return ["customers", "products", "orders", "order_items"]

@app.get("/customers", response_model=list[schemas.Customer])
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@app.post("/query")
def run_query(query: str, db: Session = Depends(get_db)):
    return run_nl_query(query, db)

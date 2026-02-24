from fastapi import FastAPI
from .routes import router
from .db import Base, engine

# Create tables if not already present
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Sales Query Agent")

# Include routes
app.include_router(router)

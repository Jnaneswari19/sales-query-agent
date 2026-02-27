import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.db import Base, SessionLocal
from app import models  
DATABASE_URL = "sqlite:///./data/sales.db"

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    engine = create_engine(DATABASE_URL)


    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
    db: Session = SessionLocal()
    alice = models.Customer(name="Alice")
    bob = models.Customer(name="Bob")
    laptop = models.Product(name="Laptop", price=1000)
    phone = models.Product(name="Phone", price=500)
    db.add_all([alice, bob, laptop, phone])
    db.commit()
    db.close()

    yield

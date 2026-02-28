from app.db import SessionLocal
from app.models import Customer

def test_db_connection():
    db = SessionLocal()
    customers = db.query(Customer).all()
    db.close()
    assert isinstance(customers, list)

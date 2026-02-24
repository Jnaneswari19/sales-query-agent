# tests/test_db.py
from app.db import SessionLocal
from app.models import Customer

db = SessionLocal()
customers = db.query(Customer).all()
print(customers)
db.close()

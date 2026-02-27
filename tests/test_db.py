from sqlalchemy import text
from app.db import SessionLocal

def test_db_connection():
    db = SessionLocal()
    result = db.execute(text("SELECT 1")).fetchone()
    assert result[0] == 1

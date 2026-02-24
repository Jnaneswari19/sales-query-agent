from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_sales():
    response = client.post("/query", json={"question": "List all customers"})
    assert response.status_code == 200
    data = response.json()
    assert "sql" in data
    assert "results" in data

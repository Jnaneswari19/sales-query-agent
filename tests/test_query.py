import pytest
from starlette.testclient import TestClient
from app.main import app
import app.llm_sql as llm_sql

client = TestClient(app)

def test_list_customers(monkeypatch):
    def fake_run_nl_query(query, db):
        return {
            "sql": "SELECT * FROM customers",
            "results": [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"}
            ]
        }

    monkeypatch.setattr(llm_sql, "run_nl_query", fake_run_nl_query)

    response = client.post("/query", json={"query": "List all customers"})
    assert response.status_code == 200
    data = response.json()
    assert data["sql"] == "SELECT * FROM customers"
    assert len(data["results"]) == 2

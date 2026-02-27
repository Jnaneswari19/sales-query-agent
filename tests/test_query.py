from fastapi.testclient import TestClient
from app.main import app
import app.llm_sql

client = TestClient(app)

def test_list_customers(monkeypatch):
    
    def fake_run_nl_query(query, db):
        return {
            "sql": "SELECT * FROM customers",
            "results": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]
        }

    monkeypatch.setattr(app.llm_sql, "run_nl_query", fake_run_nl_query)

    response = client.post("/query", json={"query": "List all customers"})
    data = response.json()
    assert "sql" in data
    assert isinstance(data.get("results", []), list)
    assert len(data["results"]) == 2

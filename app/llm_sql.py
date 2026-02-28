from app import models

def run_nl_query(query: str, db):
    
    if "customers" in query.lower():
        results = db.query(models.Customer).all()
        return {
            "sql": "SELECT * FROM customers",
            "results": [{"id": c.id, "name": c.name, "email": c.email} for c in results]
        }
    return {"sql": "UNKNOWN", "results": []}

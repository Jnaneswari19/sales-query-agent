# Sales Query Agent

![Build Status](https://github.com/yourusername/sales-query-agent/actions/workflows/tests.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A natural language interface for querying a sales database.  
Users can type questions like *“List all customers”* or *“Show me all orders for Alice”*, and the system will generate SQL, execute it, and return results.

---

## 🚀 Features
- **FastAPI backend** with REST endpoints
- **Natural language → SQL** conversion
- **SQLite database** with seeded sample data (customers, products, orders)
- **Unit tests** with `pytest` for database and query logic
- **Evaluator‑friendly repo polish**: clean structure, reproducible setup, seeded data

---

## 📂 Project Structure

```
sales-query-agent/
│
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── db.py            # Database session + Base
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── llm_sql.py       # Natural language → SQL logic
│   └── init_db.py       # Script to initialize and seed DB
│
├── data/
│   └── sales.db         # SQLite database file
│
├── tests/
│   ├── conftest.py      # Test DB setup + seeding
│   ├── test_db.py       # DB connectivity test
│   ├── test_query.py    # Query endpoint test
│
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/sales-query-agent.git
   cd sales-query-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database**
   ```bash
   python app/init_db.py
   ```

---

## ▶️ Run the App

Start FastAPI with Uvicorn:

```bash
uvicorn app.main:app --reload
```

Visit: `http://127.0.0.1:8000/docs` for interactive API docs.

---

## 🧪 Run Tests

```bash
python -m pytest
```

Expected output:
- `test_db.py` ✅ confirms DB connectivity
- `test_query.py` ✅ confirms query endpoint works with mocked SQL

---

## 📊 Example Query

**Request:**
```http
POST /query
{
  "query": "List all customers"
}
```

**Response:**
```json
{
  "sql": "SELECT * FROM customers",
  "results": [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
  ]
}
```

---

## 🏗️ Next Steps

### 1. Add More Endpoints
- Create dedicated REST endpoints for `/customers`, `/products`, and `/orders`.
- Support CRUD operations (GET, POST, PUT/PATCH, DELETE).
- Allow direct access to data without relying solely on natural language queries.

### 2. Build a Simple Frontend (React/Vue)
- Implement a lightweight UI where users can:
  - Enter natural language queries
  - View generated SQL
  - See results in a clean table
- Suggested stack: React + Axios + TailwindCSS/Bootstrap.

### 3. Expand Test Coverage with Seeded Data
- Add tests for listing products, fetching orders, and validating seeded data.
- Ensure reproducibility by seeding predictable rows in `conftest.py`.
- Cover both mocked queries and real DB queries.

### 4. Add CI/CD Workflow and Repo Badges
- Configure GitHub Actions to:
  - Run `pytest` on every push
  - Check code formatting (Black, Flake8)
  - Build and test Docker image
- Add badges to `README.md`:
  - Build status
  - Test coverage
  - Python version
  - License

---

## 📜 License
MIT License. See `LICENSE` file for details.

---

## 📦 Requirements
Dependencies are listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt
```

Key packages:
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic v2
- Pytest
- httpx, anyio
- langsmith
- python‑multipart
```


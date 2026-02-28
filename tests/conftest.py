import pytest
from app.init_db import init_db

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    init_db()

from sqlalchemy import inspect, text
from .db import engine, SessionLocal

class MCPServer:
    def __init__(self):
        self.engine = engine
        self.session = SessionLocal()

    def list_tables(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()

    def describe_schema(self, table_name: str):
        inspector = inspect(self.engine)
        return inspector.get_columns(table_name)

    def execute_query(self, sql: str):
        if not sql.strip().lower().startswith("select"):
            raise ValueError("Only SELECT statements are allowed")
        with self.engine.connect() as conn:
            result = conn.execute(text(sql))
            return [dict(row) for row in result]

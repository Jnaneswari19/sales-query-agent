from fastapi import APIRouter
from pydantic import BaseModel
from .mcp_server import MCPServer
from .llm_sql import generate_sql

router = APIRouter()
mcp = MCPServer()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_sales(req: QueryRequest):
    schema_context = {
        "tables": mcp.list_tables(),
        "schemas": {t: mcp.describe_schema(t) for t in mcp.list_tables()}
    }
    sql = generate_sql(req.question, schema_context)
    results = mcp.execute_query(sql)
    return {"sql": sql, "results": results}

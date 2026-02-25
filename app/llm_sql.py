import os
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from .db import engine

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set. Please add it to your .env file.")

# Setup LangChain SQLDatabase
db = SQLDatabase(engine)
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
sql_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

def run_nl_query(query: str, db_session: Session):
    try:
        result = sql_chain.invoke(query)   # ✅ use invoke instead of run
        return {"query": query, "result": result}
    except Exception as e:
        return {"error": str(e)}



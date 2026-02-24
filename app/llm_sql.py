import os
from langchain_anthropic import ChatAnthropic

api_key = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-3-haiku", temperature=0, api_key=api_key)

def generate_sql(question: str, schema_context: dict):
    prompt = f"""
    You are a Text-to-SQL assistant.
    User question: {question}
    Database schema: {schema_context}
    Generate a valid SQL SELECT query.
    """
    return llm.invoke(prompt).content

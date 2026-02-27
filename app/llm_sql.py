import os
import requests
from sqlalchemy.orm import Session
from sqlalchemy import text  

def run_nl_query(query: str, db: Session):
    api_key = os.getenv("OPENAI_API_KEY")
    sql = None

    prompt = f"""
    You are an expert SQL assistant.
    Translate the following natural language request into a valid SQL query for a PostgreSQL database.
    Return only the SQL query, no explanations, no comments.

    Request: {query}
    """

    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            sql = response.choices[0].message.content.strip()
        except Exception as e:
            # Fallback to Ollama
            response = requests.post(
                "http://host.docker.internal:11434/api/generate",
                json={"model": "llama3", "prompt": prompt, "stream": False}
            )
            print("Ollama raw response:", response.text)
            sql = response.json().get("response", "").strip()
    else:
        # No API key → use Ollama directly
        response = requests.post(
            "http://host.docker.internal:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        print("Ollama raw response:", response.text)
        sql = response.json().get("response", "").strip()

    # Debug logging
    print("Generated SQL:", sql)

    try:
        results = db.execute(text(sql)).fetchall()  # ✅ Wrap with text()
        return {"sql": sql, "results": [dict(r) for r in results]}
    except Exception as e:
        return {"sql": sql, "error": str(e)}

import React, { useState } from "react";
import axios from "axios";

function QueryForm() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/query", {
        query: query,
      });
      setResult(response.data);
    } catch (error) {
      setResult({ error: error.message });
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          style={{ width: "400px", padding: "0.5rem" }}
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. Show me the top 5 products by sales"
        />
        <button type="submit" style={{ marginLeft: "1rem" }}>
          Run Query
        </button>
      </form>

      {result && (
        <pre style={{ marginTop: "1rem", background: "#f4f4f4", padding: "1rem" }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default QueryForm;

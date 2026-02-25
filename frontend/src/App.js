import React from "react";
import QueryForm from "./components/QueryForm";

function App() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Sales Query Agent</h1>
      <p>Ask natural language questions about sales data:</p>
      <QueryForm />
    </div>
  );
}

export default App;

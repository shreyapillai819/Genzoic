import React, { useState } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [ticker, setTicker] = useState("");
  const [response, setResponse] = useState(null);
  const [expanded, setExpanded] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.get(\`http://localhost:8000/api/v1/market-pulse?ticker=\${ticker}\`);
    setResponse(res.data);
    setExpanded(false);
  };

  return (
    <div className="app">
      <h2>Market Pulse</h2>
      <form onSubmit={handleSubmit}>
        <input value={ticker} onChange={e => setTicker(e.target.value)} placeholder="Enter TICKER" />
        <button>Check</button>
      </form>

      {response && (
        <div className="card">
          <h3>{response.ticker} is <span className={response.pulse}>{response.pulse}</span></h3>
          <p>{response.llm_explanation}</p>
          <button onClick={() => setExpanded(!expanded)}>
            {expanded ? "Hide JSON" : "Show JSON"}
          </button>
          {expanded && (
            <pre>{JSON.stringify(response, null, 2)}</pre>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
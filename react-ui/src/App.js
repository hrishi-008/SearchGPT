import React, { useState } from "react";
import axios from "axios";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import "./App.css"; // Custom CSS file for styling and animations

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [activeResult, setActiveResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(
        "http://localhost:5000/search",
        { query },
        { timeout: 300000 } // 5-minute timeout
      );
      setResults(response.data);
      setActiveResult(0); // Automatically show the first result
    } catch (err) {
      setError("An error occurred while fetching results. Please try again.");
      console.error(err); // Log the error for debugging
    } finally {
      setLoading(false);
    }
  };

  const toggleResult = (index) => {
    setActiveResult(activeResult === index ? null : index);
  };

  return (
    <div className="app-container">
      <h1 className="title">Search GPT</h1>
      <input
        className="search-input"
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your search query"
      />
      <button
        className="search-button"
        onClick={handleSearch}
        disabled={loading}
      >
        {loading ? "Searching..." : "Search and Summarize"}
      </button>
      {error && <div className="error-message">{error}</div>}
      <div className="results-container">
        <TransitionGroup>
          {results.map((result, index) => (
            <CSSTransition
              key={index}
              timeout={500}
              classNames="result"
              unmountOnExit
            >
              <div
                className={`result-card ${
                  activeResult === index ? "active" : ""
                }`}
                onClick={() => toggleResult(index)}
              >
                <h2>Result {index + 1}</h2>
                {activeResult === index && (
                  <p className="result-content">{result}</p>
                )}
              </div>
            </CSSTransition>
          ))}
        </TransitionGroup>
      </div>
    </div>
  );
}

export default App;

import { useState } from "react";

function Practice() {
  const [input, setInput] = useState("");
  const [translation, setTranslation] = useState(null);
  const [error, setError] = useState(null);
  const [suggestions, setSuggestions] = useState([]);

  const fetchSuggestions = async (prefix) => {
    if (!prefix.trim()) {
      setSuggestions([]);
      return;
    }

    try {
      const response = await fetch(`https://mou1234.pythonanywhere.com/suggestions?prefix=${prefix}`);
      const data = await response.json();
      setSuggestions(data.suggestions || []);
    } catch {
      setSuggestions([]);
    }
  };

  const searchWord = async (word) => {
    setInput(word);
    setSuggestions([]);

    if (word.trim() === "") {
        return;
    }

    try {
      const response = await fetch(`https://mou1234.pythonanywhere.com/search?word=${word}`);
      const data = await response.json();

      if (response.ok) {
        setTranslation(`${data.translation} (Category: ${data.category})`);
        setError(null);
      } else {
        setTranslation(null);
        setError("Word not found.");
      }
    } catch {
      setError("Error fetching data.");
      setTranslation(null);
    }
  };

  return (
    <div className="page">
      <h2>Search Vocabulary</h2>
      <input
        type="text"
        placeholder="Enter a Spanish word (auto-complete)..."
        value={input}
        onChange={(e) => {
          setInput(e.target.value);
          fetchSuggestions(e.target.value);
        }}
      />
      <button className="cta-button" onClick={() => searchWord(input)}>Search</button>

      {suggestions.length > 0 && (
        <ul className="autocomplete-list">
          {suggestions.map(([word, translation], index) => (
            <li key={index} onClick={() => searchWord(word)}>
              {word} → {translation}
            </li>
          ))}
        </ul>
      )}

      {translation && <p>📖 Translation: {translation}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default Practice;
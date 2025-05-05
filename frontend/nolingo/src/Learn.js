import { useState, useEffect } from "react";

function Lessons() {
  const [word, setWord] = useState("");
  const [sentences, setSentences] = useState([]);
  const [input, setInput] = useState("");
  const [translation, setTranslation] = useState(null);
  const [error, setError] = useState(null);
  const [suggestions, setSuggestions] = useState([]);
  const [categories] = useState(["nouns", "verbs", "pronouns", "adjectives", "interrogatives", "prepositions", "phrases"]);
  const [selectedCategory, setSelectedCategory] = useState("nouns");
  const [words, setWords] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (words.length === 0) {
      setIsLoading(true);
    } else {
      setIsLoading(false);
    }
  }, [words]);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/category?name=${selectedCategory}`)
      .then((res) => res.json())
      .then((data) => setWords(data.words || []))
      .catch(() => setWords([]));
  }, [selectedCategory]);

  const fetchSuggestions = async (prefix) => {
    if (!prefix.trim()) {
      setSuggestions([]);
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:5000/suggestions?prefix=${prefix}`);
      const data = await response.json();
      setSuggestions(data.suggestions || []);
    } catch {
      setSuggestions([]);
    }
  };

  const searchWord = async (word) => {
    if (word.trim() === "") {
      return;
    }
    setInput(word);
    setWord(word);
    setSuggestions([]);

    try {
      const response = await fetch(`http://127.0.0.1:5000/search?word=${word}`);
      const data = await response.json();

      if (response.ok) {
        setTranslation(`${data.translation} [Category: ${data.category}]`);
        setError(null);
        fetchSentences(word);
      } else {
        setTranslation(null);
        setError("Word not found");
      }
    } catch {
      setError("Error fetching data");
      setTranslation(null);
    }
  };

  const clearInput = () => {
    setInput("");
    setWord("");
    setTranslation(null);
    setSentences([]);
    setError(null);
    setSuggestions([]);
  }

  const fetchSentences = async (word) => {
    if (word.trim() === "") {
        return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:5000/get_sentences?word=${word}`);
      const data = await response.json();

      if (response.ok) {
        setSentences(data.sentences);
        setError(null);
      } else {
        setSentences([]);
        setError("Sentences not found.");
      }
    } catch {
      setError("Error fetching data.");
      setSentences([]);
    }
  };

  return (
    <div className="page">
      <h2>📚 Learn</h2>
      <div className="searchAndButton">
        <input
          type="text"
          placeholder="Enter a Spanish word (auto-complete)..."
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
            fetchSuggestions(e.target.value);
          }}
        />
        {input && <button className="clear-button" onClick={() => clearInput()}>Clear</button>}
        <button className="search-button" onClick={() => searchWord(input)}>Search</button>
      </div>
        
      {suggestions.length > 0 && (
        <ul>
          {suggestions.map(([word, translation], index) => (
            <li key={index} onClick={() => searchWord(word)}>
              {word} → {translation}
            </li>
          ))}
        </ul>
      )}

      {translation && input === word &&
        <>
        <div>
          <p className="wordTranslate">{word}</p>
          <p>{translation}</p>
        </div>
        <div className="sentences">
        {sentences.length > 0 &&
          sentences.map(([spanish, translation], index) => (
            <div className="sentence" key={index}>
              <p><strong>{index+1}. {spanish}</strong></p>
              <p>{translation}</p>
            </div>
          ))
        }
        </div>
        </>
      }
      
      {input && error && <p style={{ color: "red" }}>{error}</p>}

      <select onChange={(e) => setSelectedCategory(e.target.value)} value={selectedCategory}>
        {categories.map((category) => (
          <option key={category} value={category}>
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </option>
        ))}
      </select>

      <ul>
        {words.map(([spanish, english], index) => (
          <li key={index} onClick={() => searchWord(spanish)}>
            {spanish} → {english}
          </li>
        ))}
      </ul>

      {isLoading &&
        <div className="loader">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      }
    </div>
  );
}

export default Lessons;

import { useState, useEffect } from "react";

function Lessons() {
  const [categories] = useState(["nouns", "verbs", "pronouns", "adjectives", "interrogatives", "prepositions", "phrases"]);
  const [selectedCategory, setSelectedCategory] = useState("nouns");
  const [words, setWords] = useState([]);

  useEffect(() => {
    fetch(`https://mou1234.pythonanywhere.com/category?name=${selectedCategory}`)
      .then((res) => res.json())
      .then((data) => setWords(data.words || []))
      .catch(() => setWords([]));
  }, [selectedCategory]);

  return (
    <div className="page">
      <h2>📚 Learn</h2>
      <select onChange={(e) => setSelectedCategory(e.target.value)} value={selectedCategory}>
        {categories.map((category) => (
          <option key={category} value={category}>
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </option>
        ))}
      </select>
      <ul>
        {words.map(([spanish, english], index) => (
          <li key={index}>
            {spanish} → {english}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Lessons;

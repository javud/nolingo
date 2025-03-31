import { useState, useEffect } from "react";

function Practice() {
  const [currentWord, setCurrentWord] = useState(null);
  const [translation, setTranslation] = useState("");
  const [userGuess, setUserGuess] = useState("");
  const [feedback, setFeedback] = useState("");
  const [loading, setLoading] = useState(false);
  const [showSkip, setShowSkip] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);

  useEffect(() => {
    fetchNextWord();
  }, []);

  const fetchNextWord = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5001/get_translation?word=next");
      const data = await response.json();

      if (response.ok) {
        setCurrentWord(data.translation ? data.translation.word : null);
        setTranslation(data.translation ? data.translation.translation : "");
        setFeedback("");
        setUserGuess("");
      }
    } catch (error) {
      console.error("Error fetching word:", error);
    }
    setLoading(false);
    setShowSkip(false)
  };

  const checkAnswer = () => {
    const multTranslations = translation.toLowerCase().split(",");
    const containsExactMatch = multTranslations.some(str => str.trim() === userGuess.trim().toLowerCase());
    if (containsExactMatch) {
      setFeedback("✅ Correct!");
      setCorrectCount(correctCount + 1);
      setTimeout(fetchNextWord, 750);
    } else {
      setFeedback("❌ Incorrect, try again.");
      setShowSkip(true);
    }
  };

  const skipCheck = () => {
      setFeedback("Correct Answer: " + translation);
      setTimeout(fetchNextWord, 750);
  };

  return (
    <div className="page practice">
      <h2>Practice Vocabulary</h2>
      {correctCount > 0 && <p className="correct-count">✅ {correctCount}</p>}
      {loading ? (
        <p>Loading...</p>
      ) : currentWord ? (
        <>
          <p className="word-display">Translate: <span className="wordTranslate">{currentWord}</span></p>
          <input
            autoFocus
            type="text"
            placeholder="Enter English translation..."
            value={userGuess}
            onChange={(e) => setUserGuess(e.target.value)}
            onKeyDown={(e) => {
                if (e.key === "Enter") {
                  checkAnswer();
                }
              }}
          />
          <button className="cta-button" onClick={checkAnswer}>Submit</button>
          {showSkip && <button className="cta-button-2" onClick={skipCheck}>Skip</button>}
          {feedback && <p className="feedback">{feedback}</p>}
        </>
      ) : (
        <p>No words available.</p>
      )}
    </div>
  );
}

export default Practice;

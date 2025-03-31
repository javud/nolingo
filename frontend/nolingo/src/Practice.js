import { useState, useEffect } from "react";

function Practice() {
  const [currentWord, setCurrentWord] = useState(null);
  const [translation, setTranslation] = useState("");
  const [userGuess, setUserGuess] = useState("");
  const [feedback, setFeedback] = useState("");
  const [loading, setLoading] = useState(false);
  const [showSkip, setShowSkip] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [skipCount, setSkipCount] = useState(0);
  const [wordIndex, setWordIndex] = useState(0);

  useEffect(() => {
    const fetchNextWord = async () => {
        setLoading(true);
        try {
            const response = await fetch(`https://mou1234.pythonanywhere.com/get_translation?word=next&i=${wordIndex}`);
            const data = await response.json();
        
            if (response.ok) {
                setCurrentWord(data.translation ? data.translation.word : null);
                setTranslation(data.translation ? data.translation.translation : "");
                setFeedback("");
                setUserGuess("");
            } else { // end of word list/error
                setCurrentWord(null);
                setTranslation("");
            }
        } catch (error) {
            console.error("Error fetching word:", error);
            setCurrentWord(null);
            setTranslation("");
        }
        setLoading(false);
        setShowSkip(false);
        };
        fetchNextWord();
    }, [wordIndex]);

  const reset = () => {
    setCurrentWord(null);
    setTranslation("");
    setUserGuess("");
    setFeedback("");
    setLoading(false);
    setShowSkip(false);
    setCorrectCount(0);
    setSkipCount(0);
    setWordIndex(0);
  };

  const checkAnswer = () => {
    const multTranslations = translation.toLowerCase().split(",");
    const containsExactMatch = multTranslations.some(str => str.trim() === userGuess.trim().toLowerCase());
  
    if (containsExactMatch) {
        setFeedback("✅ Correct!");
        setCorrectCount(prevCount => prevCount + 1);
        setTimeout(() => setWordIndex((prevIndex) => prevIndex + 1), 300); // fetch next word
    } else {
        setFeedback("❌ Incorrect, try again.");
        setShowSkip(true);
    }
  };

  const skipCheck = () => {
      setFeedback("Correct Answer: " + translation);
      setSkipCount(prevCount => prevCount + 1);
      setTimeout(() => setWordIndex((prevIndex) => prevIndex + 1), 500);
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
        <>
        <p>🥳 You're all caught up!</p>
        <p>Words completed: {correctCount}</p>
        <p>Words skipped: {skipCount}</p>
        <button className="cta-button" onClick={reset}>Review again</button>
        </>
      )}
    </div>
  );
}

export default Practice;

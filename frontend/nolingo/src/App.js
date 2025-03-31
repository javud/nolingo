import { BrowserRouter as Router, Routes, Route, NavLink, Link} from "react-router-dom";
import "./App.css";
import Practice from "./Practice";
import Learn from "./Learn";
import Search from "./Search";

function App() {
  return (
    <Router>
      <div className="app-container">
        <NavBar />
            <div className="page-container">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/learn" element={<Learn />} />
                <Route path="/practice" element={<Practice />} />
                <Route path="/search" element={<Search />} />
              </Routes>
            </div>
      </div>
    </Router>
  );
}

function NavBar() {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="logo">
          <img src={"/nolingo-logo.png"} alt="nolingo-logo" className={"logo"} draggable="False" />
        </Link>
        <div className="nav-links">
          <NavLink 
            to="/" 
            className={({ isActive }) => (isActive ? "selected" : "")}
          >
            Home
          </NavLink>
          <NavLink 
            to="/learn" 
            className={({ isActive }) => (isActive ? "selected" : "")}
          >
            Learn
          </NavLink>
          <NavLink 
            to="/practice" 
            className={({ isActive }) => (isActive ? "selected" : "")}
          >
            Practice
          </NavLink>
          <NavLink 
            to="/search" 
            className={({ isActive }) => (isActive ? "selected" : "")}
          >
            Search
          </NavLink>
        </div>
      </div>
    </nav>
  );
}

function Home() {
  return (
    <>
    <div className="page">
      <h1>Learn Spanish with Nolingo</h1>
      <p>Interactive learning and practice!</p>
      <Link to="/learn">
        <button className="cta-button">Start Learning</button>
      </Link>
    </div>
    <footer>Created by Javid U., Fatima J., and Syed M.</footer>
    </>
  );
}

export default App;

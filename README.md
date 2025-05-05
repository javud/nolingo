<img src="https://nolingo.netlify.app/nolingo-logo.png" alt="nolingo-logo" width="200"/>

# Nolingo: Learn Spanish Easily

## About<!-- Required -->

This application was built so that beginners who speak little to no Spanish could learn fundamentals to conversate with others. The problem we wanted to solve was how to give people the ability to practice their Spanish skills in a fun and inutitive way -- on their own time. To solve this we created Nolingo, an app that gives you control and support during your learning experience, from giving sample sentences to picture hints, all to make sure that words and sentences stick with you the next time you're speaking to someone in Spanish.

Main features: Learn and Practice tabs, learn words by category through sentences, Images for nouns, prepositions, and adjectives, translation exercises.

**Frontend:**
React (JavaScript) - offers a clean, simple template to get started with building an app. Also, very easy to deploy on static-render applications like Netlify and Vercel. Libraries used: BrowserRouter, CSSTransition, ReactDOM, useState hook, useEffect hook.

**Backend**: Flask (Python) - simple and lightweight framework, only requires 2 imports in existing Python file. API endpoints are very easy to define and use. Didn't need a heavy framework like Django (support for Object-Relational Mapper) for this project.
It is faster, as we created a lightweight app instead of a heavier one so Flask is more suited for it, and 
we wanted API support in our web app. 
Trie used for autofill in search feature to help user get the word and its sentences in the Learn tab.
Priority queue used to sort the order of words taught to user.


**Main Features:**
1. Learn: Word dictionary with over 70+ common conversational words and phrases and 400+ AI-generated sentences.
2. Practice: Interactivate learning tool where you can check your understanding of Spanish terms. Offers image hints if desired.
3. Auto-complete: Type in the start to any word or spanish phrase in Nolingo's dictionary and see all results pop-up instantly without have to type the entire term in or hitting the search button.


---

## How to use this project

The latest version of this project is deployed for free on Netlify (frontend) and PythonAnywhere (backend).
You can try it out here: https://nolingo.netlify.app/

Alternatively, if you want to use the project locally or play around with the code, the easiest way is by doing the following:

1. Open up an existing or new folder in VS Code
2. Clone the repo (click on the green button titled Code and choose your method). For additional information on how to clone repositories locally, [read this article from GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
### FRONTEND/APP (REACT) -- PART 1
1. Create a new Terminal (Terminal > New Terminal)
2. In the terminal, do one of the following:
- If it's your first-time running the code, paste these commands to go into the frontend folder & get set-up:
```bash
cd frontend/nolingo
npm install
npm start
```
- If you've already ran the frontend successfully before, you can skip the `npm install` step (since you already have the necessary modules installed on your computer):
```bash
cd frontend/nolingo
npm start
```
This will get the frontend (React app) running on your localhost. Now move onto Step 2.
### BACKEND/SERVER (FLASK) -- PART 2
1. Create a new Terminal (Terminal > New Terminal). IMPORTANT: Keep your old Terminal running, do NOT close it.
2. In the new terminal, do one of the following:
- If it's your first-time running the code, paste these commands to go into the backend folder & get set-up:
```bash
cd backend
pip install -r requirements.txt
flask --app server run
```
- If you've already ran the backend successfully before, you can skip the `pip install` step (since you already have the necessary modules installed on your computer):
```bash
cd backend
flask --app server run
```
This will get the backend (Flask server) running on your localhost (different port). You can reload the localhost page in your web browser and it should properly fetch information from the API endpoints defined in server.py.

---

## Team Contributions <!-- Required -->

- **Javid U.** - Frontend Developer. Worked on creating fluid animations, clean responsive design, and mobile compatability. Defined API endpoints in server.py and fetched information using React's fetch API.
- **Syed M.** - Project Manager. Created workflow plans, held team meetings, managed ideas and testing for the app. Assisted Javid with frontend development.
- **Fatima J.** - Backend Developer. Worked on defining the classes and methods for the key data structures used in the project (tries & priority queues). Added images for categories, adjectives, and prepositions.

---

## Demo<!-- Required -->
### YouTube Video Trailer
[![Nolingo: YouTube Ad](https://img.youtube.com/vi/KInzGWBXhd4/0.jpg)](https://youtu.be/KInzGWBXhd4)

### Learn Feature (GIF)
<img src="https://raw.githubusercontent.com/javud/nolingo/main/learnDemo.gif" alt="learn-feature-gif" width="500"/>

### Practice Feature (GIF)
<img src="https://raw.githubusercontent.com/javud/nolingo/main/practiceDemo.gif" alt="practice-feature-gif" width="500"/>

---

## Contributors<!-- Required -->
<a href="https://github.com/javud/nolingo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=javud/nolingo" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
## Acknowledgments<!-- Optional -->
The idea for Nolingo was inspired by Duolingo (not affiliated nor endorsed). Contextual sentences were generated by OpenAI's Large Language Model [ChatGPT](https://chat.openai.com/chat). Data structures were derived from UIC'S CS 351 Advanced Data Structures course taught by [Shanon Reckinger](https://cs.uic.edu/profiles/shanon-reckinger/).

## Connect<!-- Required -->
To provide feedback on the repo (issues, comments, improvements), please contact us either via LinkedIn or email.

- **Javid Uddin** – [LinkedIn](https://linkedin.com/in/javiduddin) [Email](mailto:muddi7@uic.edu)
- **Syed Muqtadeer** – [LinkedIn](https://www.linkedin.com/in/syed-muqtadeer-59b289221/) [Email](mailto:smuqt2@uic.edu)
- **Fatima Jassim** – [LinkedIn](https://www.linkedin.com/in/fatima-jassim/) [Email](mailto:fjass2@uic.edu)

<!-- - Use this html element to create a back to top button. -->
<p align="right"><a href="#how-to-use-this-project">back to top ⬆️</a></p>

---


## License<!-- Optional -->
<!-- 
* Here you can add project license for copyrights and distribution 
* 
* check this website for an easy reference https://choosealicense.com/)
-->
MIT License

Copyright (c) [2025] [Nolingo]

<!-- - Use this html element to create a back to top button. -->
<p align="right"><a href="#how-to-use-this-project">back to top ⬆️</a></p>

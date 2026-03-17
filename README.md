# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose: 
	The purpose of this game is to guess the secret number the game generates. The game will reward you points based on how many guesses it takes for you to get the right answer. The game will also help you out by letting you know whether you need to go higher or lower in a guess. 
- [ ] Detail which bugs you found: 
	Some examples of bugs I found swapped ranges, swapped messages telling the user to go up or down for the wrong inputs, and unnecessary if/else statements incorrectly separating scores. 
- [ ] Explain what fixes you applied: 
	Based on the bugs I identified, I was able to correct the ranges, swap statements to their correct conditionals, and reduce unnecessary code to make sure that scores are distributed correctly. 

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

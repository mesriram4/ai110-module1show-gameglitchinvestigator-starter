# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?: 
  + For starters, when switching between Easy, Medium, and Hard, the ranges expected for each mode did not align with what was displayed on the blue message box. 
  + Easy, Medium, and Hard modes should also have consistent numbers of guesses associated with them --> easy should have more attempts than medium and hard, but this wasn't the case when running the game for the first time. 
  + Medium should have a range of 1 to 50, and hard should have a range of 1  to 100. This wasn't the case when running the game for the first time. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  + Interestingly, regardless of the number I guess, I'm getting the response "Go Higher". Even if I type in 100, I'm getting the message "Go Higher" 
  + Attepts tracker in the blue box vs. developer are not in line with each other.
  + The second time I ran it, my game is not running the same way it should be during it's first round. Even though it resets info for a new game, my game isn't accepting inputs, neither is it displaying hints after I submit an input. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?: 
  + I used Claude AI for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

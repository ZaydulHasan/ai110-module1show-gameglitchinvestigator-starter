# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it launched but had several obvious problems. The hints were backwards — when I guessed too high, it told me to go higher instead of lower. The score and game status did not reset when clicking "New Game", so the game kept saying "You already won" even in a fresh game. Additionally, the secret number was being randomly converted to a string on even-numbered attempts, which caused comparisons to break silently.

---

## 2. How did you use AI as a teammate?

I used Claude as my AI assistant throughout this project. One correct suggestion was fixing the `check_guess` function to return "Too High" with "Go LOWER!" — I verified this by running pytest and all 3 tests passed. One misleading aspect was that the starter code already had a `check_guess` function in `app.py` with the same name as one in `logic_utils.py`, which caused confusion about which one was actually being called — I had to carefully trace the imports to understand which file mattered.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both the automated pytest tests passed AND the live game behaved correctly in the browser. For example, I ran `py -m pytest` after fixing the inverted hints and confirmed all 3 tests passed. I also manually tested by entering a guess higher than the secret number and verifying the hint now correctly said "Go LOWER!". Claude helped me understand that `check_guess` returns a tuple, so tests needed to check `result[0]` instead of just `result`.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every single time a user clicks a button or interacts with the app. T
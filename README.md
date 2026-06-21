# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation
An AI built a number guessing game using Streamlit. It was full of bugs:
hints lied, the secret kept changing, Hard mode was easier than Normal,
and the logic file was full of placeholder crashes.

## 🛠️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the fixed app: `python -m streamlit run app.py`

## 📝 Document Your Experience
This is a Streamlit number-guessing game. The player picks a difficulty,
then guesses a secret number within a limited number of attempts. The game
gives correct High/Low hints and tracks a score.

Bugs found and fixed:
- Bug 1: Hints were backwards — "Go HIGHER!" shown when guess was too high
- Bug 2: Secret number reset on every interaction — game was unwinnable
- Bug 3: Hard mode had range 1–50, easier than Normal's 1–100, fixed to 1–200
- Bug 4: logic_utils.py had only NotImplementedError stubs — real logic moved in

## 📸 Demo Walkthrough
1. User selects Normal difficulty (range 1–100, 8 attempts)
2. Secret number is generated (e.g., 8) and stays fixed the whole game
3. User enters 50 and clicks Submit — game shows "📉 Go LOWER!" (correct!)
4. User enters 3 — game shows "📈 Go HIGHER!" (correct!)
5. User enters 8 — game shows "🎉 Correct! You guessed it!" — win screen appears
6. Score updates and Guess History shows all previous guesses
7. User clicks Play Again to start a fresh round

## 🧪 Test Results
pytest tests/
========================= 12 passed in 0.04s =========================

## 🚀 Stretch Features
No stretch features completed for this submission.
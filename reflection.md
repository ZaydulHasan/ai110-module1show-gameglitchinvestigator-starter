# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the hints were completely backwards. The game also had
no working submit button in the original code, and the secret number kept resetting
on every interaction. The logic_utils.py file had no real code — every function
just raised a NotImplementedError, which made all tests crash immediately.

**Bug 1 — Backwards hints:** When I guessed 80 with a secret of 30, the game said
"Go HIGHER!" instead of "Go LOWER!" The comparison logic was correct but the
returned messages were swapped.

**Bug 2 — Secret number resets:** Every time I clicked New Game, the secret changed
to a completely new random number, making the game impossible to win.

### Bug Reproduction Log

| Input Used | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Guess of 80 (secret=30) | "Too High — Go LOWER" | "Too High — Go HIGHER!" | none |
| Click New Game 3 times | Secret stays fixed | Secret changes every click | none |
| Select Hard difficulty | Range 1–200 (harder) | Range 1–50 (easier than Normal) | none |
| Run pytest | Tests pass | NotImplementedError in logic_utils.py | ModuleNotFoundError |

## 2. How did you use AI as a teammate?

I used Claude as my AI coding assistant throughout this project.

**Correct suggestion:** Claude correctly identified that in check_guess(), the return
values "Go HIGHER!" and "Go LOWER!" were swapped relative to the condition
`if guess > secret`. I verified this by running the game — guessing 80 with a
secret of 30 showed "Go HIGHER!" which confirmed the bug. After the fix, the same
guess correctly showed "Go LOWER!"

**Incorrect/misleading suggestion:** Claude initially suggested using
`st.experimental_rerun()` which is deprecated in newer versions of Streamlit.
I verified this was wrong by checking that `st.rerun()` is the correct modern
function and used that instead.

## 3. Debugging and testing your fixes

I confirmed each fix two ways: first by running pytest to check the logic in
isolation, and second by running the live Streamlit app and playing the game.
For the backwards hints bug, my test `test_guess_too_high` asserted that the
message contains "LOWER" — this would fail with the original code and pass after
the fix. All 12 tests passed after the fixes were applied.

## 4. What did you learn about Streamlit and state?

Streamlit works by re-running the entire Python script from top to bottom every
time a user interacts with the app — like calling main() again in C++. This means
any regular variable gets reset on each interaction. st.session_state is a
dictionary that persists between reruns like a global variable, so you must store
anything you want to keep (like the secret number or attempt count) in it, and
always guard initialization with `if "key" not in st.session_state` so it only
sets the value once.

## 5. Looking ahead: your developer habits

One habit I will reuse is writing test cases that confirm a bug exists before
fixing it — this ensures the fix actually addresses the root cause and didn't
just mask the problem. Next time I work with AI on a coding task, I will ask it
to explain WHY a change is needed, not just WHAT to change, so I can properly
evaluate whether the suggestion makes sense.

This project changed how I think about AI-generated code — even a seemingly
working snippet can have subtle logic inversions like the hint bug that look
correct at first glance. Human review of the actual behavior is always essential.
import random
import streamlit as st

# FIX: Import all logic from logic_utils.py instead of defining it here
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

# --- Sidebar Settings ---
st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# --- Session State Initialization ---
# FIX: This solves the secret number reset bug.
# Streamlit reruns the whole script on every click (like calling main() again in C++).
# st.session_state is like a global variable that SURVIVES between reruns.
# The "if not in" guard means we only set it ONCE, not on every rerun.

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

# --- Game UI ---
st.subheader("Make a guess")

attempts_left = attempt_limit - st.session_state.attempts + 1
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

# --- Game Over Screens ---
if st.session_state.status == "won":
    st.success(f"🎉 You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
    if st.button("Play Again"):
        st.session_state.secret = random.randint(low, high)
        st.session_state.attempts = 1
        st.session_state.score = 0
        st.session_state.status = "playing"
        st.session_state.history = []
        st.rerun()

elif st.session_state.status == "lost":
    st.error(f"💀 Game over! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
    if st.button("Play Again"):
        st.session_state.secret = random.randint(low, high)
        st.session_state.attempts = 1
        st.session_state.score = 0
        st.session_state.status = "playing"
        st.session_state.history = []
        st.rerun()

else:
    # --- Active Gameplay ---
    raw_input = st.text_input("Enter your guess:")

    if st.button("Submit Guess 🚀"):
        ok, guess_value, error_msg = parse_guess(raw_input)

        if not ok:
            st.warning(error_msg)
        else:
            # FIX: check_guess now from logic_utils with corrected hints
            outcome, message = check_guess(guess_value, st.session_state.secret)

            st.session_state.score = update_score(
                st.session_state.score, outcome, st.session_state.attempts
            )

            st.session_state.history.append({
                "attempt": st.session_state.attempts,
                "guess": guess_value,
                "outcome": outcome,
                "message": message,
            })

            if outcome == "Win":
                st.session_state.status = "won"
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
            else:
                st.session_state.attempts += 1

            st.rerun()

# --- Guess History ---
if st.session_state.history:
    st.subheader("Guess History")
    for entry in st.session_state.history:
        st.write(f"Attempt {entry['attempt']}: Guessed {entry['guess']} → {entry['message']}")

# --- Developer Debug Info ---
with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)
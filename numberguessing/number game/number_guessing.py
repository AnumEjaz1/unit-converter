import streamlit as st
import random

# Initialize session state variables
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 10  # Default attempts
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = "I'm thinking of a number between 1 and 100. Can you guess it?"
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"

st.title("🎯 Number Guessing Game")
st.write("Try to guess the number I am thinking of!")

# Difficulty selection
difficulty = st.radio("Choose Difficulty Level:", ["Easy", "Hard"], index=0)

if st.button("Set Difficulty"):
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 10 if difficulty == "Easy" else 5
    st.session_state.answer = random.randint(1, 100)  # Reset the answer
    st.session_state.game_over = False
    st.session_state.message = f"Difficulty set to {difficulty}. Start guessing!"
    st.rerun()  # ✅ Updated function

st.write(f"💡 {st.session_state.message}")
st.write(f"🔢 Attempts remaining: {st.session_state.attempts}")

# User input for guessing
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        if guess == st.session_state.answer:
            st.session_state.message = f"🎉 Correct! The number was {st.session_state.answer}."
            st.session_state.game_over = True
        elif guess < st.session_state.answer:
            st.session_state.message = "📉 Too low! Try again."
            st.session_state.attempts -= 1
        else:
            st.session_state.message = "📈 Too high! Try again."
            st.session_state.attempts -= 1

        if st.session_state.attempts == 0 and not st.session_state.game_over:
            st.session_state.message = f"❌ Game Over! The correct number was {st.session_state.answer}."
            st.session_state.game_over = True

        st.rerun()  # ✅ Updated function

# Reset Button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.answer = random.randint(1, 100)
        st.session_state.attempts = 10 if st.session_state.difficulty == "Easy" else 5
        st.session_state.game_over = False
        st.session_state.message = "I'm thinking of a number between 1 and 100. Can you guess it?"
        st.rerun()  # ✅ Updated function

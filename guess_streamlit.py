import random
import streamlit as st

st.title("NUMBER GUESSING GAME!!!!")

guess = st.number_input("guess a number between 1 and 100", min_value=1, max_value=100, step=1)

if st.button("check"):
    num = random.randint(1, 100)
    if guess == num:
        st.write("CORRECT")
    elif guess < num:
        st.write("Too small")
    elif guess > num:
        st.write("Too big ")
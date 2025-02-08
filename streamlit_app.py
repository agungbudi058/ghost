import streamlit as st
import os
import sys
import subprocess

st.title("Avoid the Ghosts! 🎮")
st.write("Click 'Start Game' to play. A new game window will open.")

# Button to launch the game
if st.button("Start Game"):
    game_script = os.path.join(os.path.dirname(__file__), "game.py")
    subprocess.Popen([sys.executable, game_script])
    st.write("Game launched! If the window does not appear, check your taskbar.")

import streamlit as st


def render_scoreboard() -> None:
    """Render the X/O win counts and draw count as metric cards."""
    scores = st.session_state.scores
    col1, col2, col3 = st.columns(3)
    col1.metric("X Wins", scores["X"])
    col2.metric("O Wins", scores["O"])
    col3.metric("Draws", scores["Draw"])

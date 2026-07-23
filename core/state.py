import streamlit as st


def init_state() -> None:
    """Initialize all Streamlit session_state keys used by the game.
    Safe to call on every rerun -- only sets a key if it isn't
    already present, so in-progress games and scores survive reruns.
    """
    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"
    if "game_over" not in st.session_state:
        st.session_state.game_over = False
    if "message" not in st.session_state:
        st.session_state.message = "Player X's turn"
    if "scores" not in st.session_state:
        st.session_state.scores = {
            "X": 0,
            "O": 0,
            "Draw": 0,
        }

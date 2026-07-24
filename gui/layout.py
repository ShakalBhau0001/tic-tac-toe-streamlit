import streamlit as st
from gui.scoreboard import render_scoreboard
from gui.board import render_board
from gui.styles import inject_cell_colors
from core.game import new_game


def render_ui() -> None:
    """Render the full page: title, scoreboard, board, and reset button."""
    st.set_page_config(
        page_title="Tic Tac Toe",
        page_icon="❌",
        layout="centered",
    )

    st.title("❌ Tic Tac Toe ⭕")
    st.subheader(st.session_state.message)

    render_scoreboard()
    inject_cell_colors()
    render_board()

    st.divider()
    st.button(
        "🔄 New Game",
        on_click=new_game,
        use_container_width=True,
    )

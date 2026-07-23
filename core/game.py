import streamlit as st
from core.constants import WIN_COMBINATIONS


def check_winner(player: str) -> bool:
    """Return True if `player` ('X' or 'O') occupies any winning line."""
    board = st.session_state.board
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_board_full() -> bool:
    """Return True if every cell on the board has been played."""
    return "" not in st.session_state.board


def handle_move(index: int) -> None:
    """Play the current player's move on `index`, then update game state.
    No-ops if the game has already ended or the cell is occupied.
    Updates the winner/draw message, score tally, and whose turn it
    is next, all via st.session_state.
    """
    if st.session_state.game_over:
        return

    if st.session_state.board[index] != "":
        return

    st.session_state.board[index] = st.session_state.current_player

    if check_winner(st.session_state.current_player):
        winner = st.session_state.current_player
        st.session_state.message = f"Player {winner} wins! 🎉"
        st.session_state.game_over = True
        st.session_state.scores[winner] += 1
        return

    if is_board_full():
        st.session_state.message = "It's a draw! 🤝"
        st.session_state.game_over = True
        st.session_state.scores["Draw"] += 1
        return

    st.session_state.current_player = (
        "O" if st.session_state.current_player == "X" else "X"
    )
    st.session_state.message = (
        f"Player {st.session_state.current_player}'s turn"
    )


def new_game() -> None:
    """Reset the board and turn state for a fresh round (scores persist)."""
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.message = "Player X's turn"

"""Integration tests for Tic-Stream, driven through the real UI via
Streamlit's AppTest -- no logic is mocked, so these exercise the actual
click -> handle_move -> rerender path a user would trigger in the browser.

Run with: pytest
"""
from streamlit.testing.v1 import AppTest


def _fresh_app() -> AppTest:
    at = AppTest.from_file("main.py")
    at.run()
    return at


def test_initial_state():
    at = _fresh_app()
    assert at.session_state.board == [""] * 9
    assert at.session_state.current_player == "X"
    assert at.session_state.message == "Player X's turn"
    assert not at.session_state.game_over


def test_x_wins_top_row():
    at = _fresh_app()
    # X: 0, 1, 2 | O: 3, 4
    for cell in (0, 3, 1, 4, 2):
        at.button(key=f"cell_{cell}").click().run()

    assert at.session_state.game_over
    assert "Player X wins" in at.session_state.message
    assert at.session_state.scores["X"] == 1


def test_draw_has_no_winner():
    at = _fresh_app()
    # X O X / X O O / O X X -> full board, no line for either player
    for cell in (0, 1, 2, 4, 3, 5, 7, 6, 8):
        at.button(key=f"cell_{cell}").click().run()

    assert at.session_state.game_over
    assert "draw" in at.session_state.message.lower()
    assert at.session_state.scores["Draw"] == 1


def test_occupied_and_post_game_clicks_are_ignored():
    at = _fresh_app()
    at.button(key="cell_0").click().run()  # X plays 0

    # Clicking the same cell again should not hand the turn to X twice
    at.button(key="cell_0").click().run()
    assert at.session_state.board[0] == "X"
    assert at.session_state.current_player == "O"


def test_new_game_resets_board_but_keeps_scores():
    at = _fresh_app()
    for cell in (0, 3, 1, 4, 2):  # X wins
        at.button(key=f"cell_{cell}").click().run()

    reset_btn = [b for b in at.button if "New Game" in b.label][0]
    reset_btn.click().run()

    assert at.session_state.board == [""] * 9
    assert not at.session_state.game_over
    assert at.session_state.scores["X"] == 1  # score persists

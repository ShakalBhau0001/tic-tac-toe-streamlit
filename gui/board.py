import streamlit as st
from core.game import handle_move


def render_board() -> None:
    """Render the 3x3 grid of cell buttons and wire them to handle_move."""
    for row in range(3):
        cols = st.columns(3, gap="small")
        for col in range(3):
            index = row * 3 + col
            value = st.session_state.board[index]
            label = value if value else " "
            with cols[col]:
                st.button(
                    label,
                    key=f"cell_{index}",
                    on_click=handle_move,
                    args=(index,),
                    use_container_width=True,
                    disabled=(
                        st.session_state.game_over
                        or value != ""
                    ),
                )

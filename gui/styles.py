import streamlit as st
from core.constants import X_COLOR, O_COLOR


def inject_cell_colors() -> None:
    """Inject CSS so played cells show X in red / O in green.
    Targets each button via Streamlit's `st-key-<key>` selector, which
    requires Streamlit >= 1.30.
    """
    css_rules = []
    for index, value in enumerate(st.session_state.board):
        if value == "X":
            color = X_COLOR
        elif value == "O":
            color = O_COLOR
        else:
            continue

        css_rules.append(
            f"""
            .st-key-cell_{index} button{{
                background-color:{color}!important;
                color:white!important;
                border-color:{color}!important;
            }}
            """
        )
    if css_rules:
        st.markdown(
            f"<style>{''.join(css_rules)}</style>",
            unsafe_allow_html=True,
        )

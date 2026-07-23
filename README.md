# tic-tac-toe-streamlit
A modular Tic Tac Toe web application built with Python and Streamlit, featuring an interactive responsive UI, reusable components, session state management, a live scoreboard, and a clean, scalable architecture following software engineering best practices.

---

## 📂 Project Structure

```
tic-tac-toe-streamlit/
├── main.py                # Entry point — wires state + UI together
├── core/                   # Game logic — no Streamlit UI concerns
│   ├── __init__.py          # Empty File
│   ├── constants.py          # Win combinations, cell colours
│   ├── state.py               # session_state initialization
│   └── game.py                 # Move handling, win/draw detection, reset
├── gui/                    # Presentation layer
│   ├── __init__.py          # Empty File
│   ├── layout.py             # Page scaffold (title, sections, reset button)
│   ├── board.py                # 3x3 button grid
│   ├── scoreboard.py            # X/O/Draw score metrics
│   └── styles.py                 # Dynamic per-cell CSS injection
├── tests/
│   └── test_game.py         # End-to-end tests via Streamlit's AppTest
├── requirements.txt        # Runtime & Test dependency
└── .gitignore
```

---

> **Note :-  Work In Progress ...**

---

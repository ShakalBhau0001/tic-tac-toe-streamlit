from core.state import init_state
from gui.layout import render_ui


def main() -> None:
    """Entry point: initialize session state and render the app."""
    init_state()
    render_ui()


if __name__ == "__main__":
    main()

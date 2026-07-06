"""
Stock-CIO

Application Entry Point
"""

from src.core.cio_engine import CIOEngine


def main() -> int:
    """Application entry point."""

    engine = CIOEngine()
    engine.run()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
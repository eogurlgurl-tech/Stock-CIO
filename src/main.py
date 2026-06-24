"""
Stock-CIO

Entry Point
"""

from core.cio_engine import CIOEngine


def main() -> int:
    """Application entry point."""

    engine = CIOEngine()
    engine.start()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
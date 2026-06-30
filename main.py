"""
Stock-CIO

Application Entry Point
"""

from src.core.cio_engine import CIOEngine


def main() -> int:

    engine = CIOEngine()
    engine.start()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
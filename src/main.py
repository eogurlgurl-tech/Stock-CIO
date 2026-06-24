"""
Stock-CIO

AI Chief Investment Officer System

Version : v0.1 Alpha
"""

from datetime import datetime


class StockCIO:

    VERSION = "v0.1 Alpha"

    def start(self) -> None:
        """Start Stock-CIO."""

        print("=" * 50)
        print("📈 Stock-CIO")
        print("AI Chief Investment Officer System")
        print(f"Version : {self.VERSION}")
        print(f"Start Time : {datetime.now():%Y-%m-%d %H:%M:%S}")
        print("Status : READY")
        print("=" * 50)


def main() -> None:
    app = StockCIO()
    app.start()


if __name__ == "__main__":
    main()
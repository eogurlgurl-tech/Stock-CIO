"""
STOCK-CIO Desktop Entry Point
"""

import os
import sys
from pathlib import Path
from tkinter import Tk

from src.desktop.stock_cio_app import StockCIOApp


def application_root() -> Path:
    """Return the source or packaged application root."""

    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent


def main() -> int:
    """Start the STOCK-CIO desktop application."""

    os.chdir(application_root())

    root = Tk()
    StockCIOApp(root)
    root.mainloop()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

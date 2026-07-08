"""
Web interface for STOCK-CIO.
"""

from __future__ import annotations

import contextlib
import io
from datetime import datetime

from flask import Flask, redirect, render_template, url_for

from src.core.cio_engine import CIOEngine


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    last_run: dict[str, str | None] = {"output": None, "timestamp": None}

    @app.route("/", methods=["GET"])
    def index() -> str:
        return render_template(
            "dashboard.html",
            output=last_run["output"],
            timestamp=last_run["timestamp"],
        )

    @app.route("/run", methods=["POST"])
    def run_analysis() -> str:
        buffer = io.StringIO()
        engine = CIOEngine()

        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
            engine.run()

        last_run["output"] = buffer.getvalue()
        last_run["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return redirect(url_for("index"))

    return app

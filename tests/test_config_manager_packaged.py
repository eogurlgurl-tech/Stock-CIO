"""
Unit Tests for Packaged Configuration

Module : Config Manager
"""

import sys
from pathlib import Path

from src.config.config_manager import ConfigManager


def test_source_application_root():
    """Source mode uses the repository root."""

    root = ConfigManager._application_root()

    assert (root / "10_CONFIG").is_dir()


def test_packaged_application_root(monkeypatch, tmp_path):
    """Packaged mode uses the executable directory."""

    executable = tmp_path / "STOCK-CIO.exe"
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(executable))

    root = ConfigManager._application_root()

    assert root == Path(tmp_path)


def test_packaged_config_dir_falls_back_to_ancestor(monkeypatch, tmp_path):
    """Packaged mode finds 10_CONFIG in an ancestor directory."""

    executable = tmp_path / "dist" / "주식-CIO" / "STOCK-CIO.exe"
    executable.parent.mkdir(parents=True)
    config_dir = tmp_path / "10_CONFIG"
    config_dir.mkdir()
    (config_dir / "weight.yaml").write_text("key: value\n", encoding="utf-8")

    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(executable))

    manager = ConfigManager()

    assert manager.config_dir == config_dir

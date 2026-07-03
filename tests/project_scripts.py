"""
Tests for Developer Automation scripts.

STOCK-CIO
"""

from scripts.finish_feature import main as finish_feature_main
from scripts.update_changelog import ChangeLogGenerator
from scripts.update_next_task import NextTaskGenerator
from scripts.update_session import SessionGenerator
from scripts.update_status import StatusGenerator
from scripts.utils.project_info import load_project_info
from scripts.utils.state import ProjectState


def test_load_project_info() -> None:
    """Project information should load successfully."""

    info = load_project_info()

    assert info.root.exists()
    assert info.docs.exists()
    assert info.src.exists()
    assert info.tests.exists()


def test_load_project_state() -> None:
    """Project state should load successfully."""

    state = ProjectState.load()

    assert state.project.name
    assert state.project.version
    assert state.current.sprint
    assert state.current.feature
    assert state.build.status
    assert state.build.tests


def test_status_generator() -> None:
    """STATUS.md should be generated."""

    output = StatusGenerator().write()

    assert output.exists()
    assert output.name == "STATUS.md"


def test_session_generator() -> None:
    """SESSION.md should be generated."""

    output = SessionGenerator().write()

    assert output.exists()
    assert output.name == "SESSION.md"


def test_next_task_generator() -> None:
    """NEXT_TASK.md should be generated."""

    output = NextTaskGenerator().write()

    assert output.exists()
    assert output.name == "NEXT_TASK.md"


def test_changelog_generator() -> None:
    """CHANGELOG.md should be generated."""

    output = ChangeLogGenerator().write()

    assert output.exists()
    assert output.name == "CHANGELOG.md"


def test_finish_feature() -> None:
    """finish_feature should complete successfully."""

    result = finish_feature_main()

    assert result == 0


def test_generated_documents_exist() -> None:
    """Generated documents should exist."""

    docs = load_project_info().docs

    expected = (
        "STATUS.md",
        "SESSION.md",
        "NEXT_TASK.md",
        "CHANGELOG.md",
    )

    for filename in expected:
        assert (docs / filename).exists()
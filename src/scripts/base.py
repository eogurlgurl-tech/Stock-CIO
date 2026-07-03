"""
Developer Automation Framework

Provides common abstractions and runner for all automation tasks.

STOCK-CIO
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import perf_counter


@dataclass(frozen=True, slots=True)
class TaskResult:
    """Execution result of a single automation task."""

    name: str
    success: bool
    elapsed_seconds: float
    message: str = ""


class AutomationTask(ABC):
    """Base class for all automation tasks."""

    @property
    def name(self) -> str:
        """Return the task name."""
        return self.__class__.__name__

    @abstractmethod
    def run(self) -> None:
        """Execute the task."""


class AutomationRunner:
    """Runs automation tasks sequentially."""

    def __init__(self, *tasks: AutomationTask) -> None:
        self._tasks = list(tasks)

    def add_task(self, task: AutomationTask) -> None:
        """Register an additional task."""
        self._tasks.append(task)

    def run_all(self) -> list[TaskResult]:
        """
        Execute every registered task.

        Returns
        -------
        list[TaskResult]
            Execution results in the order tasks were run.

        Raises
        ------
        Exception
            Re-raises the first exception encountered after recording
            the failed task result.
        """

        results: list[TaskResult] = []

        for task in self._tasks:
            start = perf_counter()

            try:
                task.run()

            except Exception as exc:
                elapsed = perf_counter() - start

                results.append(
                    TaskResult(
                        name=task.name,
                        success=False,
                        elapsed_seconds=elapsed,
                        message=str(exc),
                    )
                )

                raise

            elapsed = perf_counter() - start

            results.append(
                TaskResult(
                    name=task.name,
                    success=True,
                    elapsed_seconds=elapsed,
                )
            )

        return results
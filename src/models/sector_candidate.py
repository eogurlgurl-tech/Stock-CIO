"""
Sector Candidate Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SectorCandidate:
    """추천 섹터"""

    name: str

    score: int

    reason: str
"""Core grade calculations."""
import os


def average(scores):
    """Return the mean of a list of scores."""
    return sum(scores) / len(scores)


def validate_score(score):
    """Raise ValueError if a score is outside 0-100."""
    if score < 0 or score > 100:
        raise ValueError(f"Score {score} must be between 0 and 100")
    return score

"""Core grade calculations."""
import os


def average(scores):
    """Return the mean of a list of scores, rounded to 1 decimal place."""
    return round(sum(scores) / len(scores), 1)


def validate_score(score):
    """Raise ValueError if a score is outside 0-100."""
    if score < 0 or score > 100:
        raise ValueError(f"Score {score} must be between 0 and 100")
    return score


def letter_grade(score):
    """Convert a numeric score to a letter grade (WAEC-style bands)."""
    validate_score(score)
    if score >= 75:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

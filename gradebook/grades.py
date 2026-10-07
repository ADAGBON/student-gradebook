"""Core grade calculations."""


def average(scores):
    """Return the mean of a list of scores, rounded to 1 decimal place.

    Raises ValueError if the list is empty.
    """
    if not scores:
        raise ValueError("Cannot average an empty list of scores")
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


def class_summary(scores):
    """Return a summary dict for a class: count, average, highest, lowest, pass rate."""
    if not scores:
        raise ValueError("Cannot summarise an empty class")
    for s in scores:
        validate_score(s)
    passed = sum(1 for s in scores if s >= 40)
    return {
        "count": len(scores),
        "average": average(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "pass_rate": round(passed / len(scores) * 100, 1),
    }

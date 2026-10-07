from gradebook.grades import average, letter_grade, validate_score
import pytest


def test_average_of_simple_list():
    assert average([70, 80, 90]) == 80


def test_validate_score_accepts_valid_score():
    assert validate_score(55) == 55


def test_validate_score_rejects_out_of_range():
    with pytest.raises(ValueError):
        validate_score(105)


@pytest.mark.parametrize(
    "score, expected",
    [(100, "A"), (75, "A"), (74, "B"), (65, "B"), (50, "C"), (40, "D"), (39, "F"), (0, "F")],
)
def test_letter_grade_boundaries(score, expected):
    assert letter_grade(score) == expected


def test_letter_grade_rejects_invalid_score():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_average_of_empty_list_raises():
    with pytest.raises(ValueError):
        average([])

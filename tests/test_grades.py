import pytest

from gradebook.grades import average, class_summary, letter_grade, validate_score


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


def test_average_is_rounded_to_one_decimal():
    assert average([70, 80, 81]) == 77.0
    assert average([1, 2, 2]) == 1.7


def test_class_summary_values():
    result = class_summary([35, 50, 80, 95])
    assert result == {
        "count": 4,
        "average": 65.0,
        "highest": 95,
        "lowest": 35,
        "pass_rate": 75.0,
    }


def test_class_summary_rejects_empty_class():
    with pytest.raises(ValueError):
        class_summary([])


def test_class_summary_rejects_invalid_score():
    with pytest.raises(ValueError):
        class_summary([50, 120])

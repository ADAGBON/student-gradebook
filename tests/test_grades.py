from gradebook.grades import average, validate_score
import pytest


def test_average_of_simple_list():
    assert average([70, 80, 90]) == 80


def test_validate_score_accepts_valid_score():
    assert validate_score(55) == 55


def test_validate_score_rejects_out_of_range():
    with pytest.raises(ValueError):
        validate_score(105)

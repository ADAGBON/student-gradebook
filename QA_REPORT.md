# QA Report – Student Gradebook

## 1. Summary

| Check | Tool | Result |
|---|---|---|
| Unit tests | pytest | **18 passed, 0 failed** |
| Coverage | pytest-cov | **97%** (gate: 90%) |
| Lint | ruff check (rules E, W, F, I, B, UP) | 2 issues found → fixed → **0 remaining** |
| Formatting | ruff format | 2 files reformatted → **all formatted** |
| Build | `python -m compileall` + CLI smoke test | **Passing** |
| CI | GitHub Actions, Python 3.11 & 3.12 | Runs on every push and pull request |

## 2. Unit tests written

**`tests/test_grades.py`**

| Function | Test | What it proves |
|---|---|---|
| `average` | `test_average_of_simple_list` | Mean of `[70, 80, 90]` is 80 |
| `average` | `test_average_is_rounded_to_one_decimal` | `[1, 2, 2]` → 1.7, not 1.666… |
| `average` | `test_average_of_empty_list_raises` | Empty list gives a clear `ValueError`, not `ZeroDivisionError` |
| `validate_score` | `test_validate_score_accepts_valid_score` | Valid scores pass through unchanged |
| `validate_score` | `test_validate_score_rejects_out_of_range` | 105 is rejected |
| `letter_grade` | `test_letter_grade_boundaries` (8 cases) | Every grade boundary: 100, 75, 74, 65, 50, 40, 39, 0 |
| `letter_grade` | `test_letter_grade_rejects_invalid_score` | −1 is rejected |
| `class_summary` | `test_class_summary_values` | Count, average, highest, lowest and pass rate for a sample class |
| `class_summary` | `test_class_summary_rejects_empty_class` | Empty class is rejected |
| `class_summary` | `test_class_summary_rejects_invalid_score` | A score of 120 anywhere in the class is rejected |

**`tests/test_cli.py`**

| Test | What it proves |
|---|---|
| `test_cli_prints_average_and_grade` | `python -m gradebook 70 80 90` prints `Average: 80.0 -> Grade A` |

Boundary testing was the most valuable technique: the grade bands change at 75, 65, 50
and 40, so each test checks the value exactly on the boundary and one below it.

**Coverage**

```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
gradebook/__init__.py       0      0   100%
gradebook/__main__.py      10      1    90%   17
gradebook/grades.py        26      0   100%
-----------------------------------------------------
TOTAL                      36      1    97%
```

The single uncovered line is the `if __name__ == "__main__"` guard, which is exercised
by the CI smoke-test step instead of a unit test.

## 3. Linter findings

Ruff was added on branch `chore/linting` and run against the existing code before any
fixes. Output:

```
gradebook/grades.py:2:8: F401 [*] `os` imported but unused
tests/test_grades.py:1:1: I001 [*] Import block is un-sorted or un-formatted
Found 2 errors.

2 files would be reformatted (gradebook/__main__.py, gradebook/grades.py)
```

| Rule | File | Issue | Fix |
|---|---|---|---|
| F401 | `gradebook/grades.py` | `import os` was never used | Removed the import |
| I001 | `tests/test_grades.py` | Third-party `pytest` imported after local `gradebook` | Re-ordered: standard library → third-party → local |
| Format | `gradebook/__main__.py`, `gradebook/grades.py` | Missing blank line after module docstring | Applied `ruff format` |

After commit `style: fix lint findings…`, `ruff check .` reports **All checks passed**
and CI now fails any future push that reintroduces these problems.

## 4. Code reviews

Every change was made on its own branch and merged into `main` through a pull request
using the checklist in `.github/pull_request_template.md`.

| Branch / PR | Reviewer focus | Findings | Outcome |
|---|---|---|---|
| `feature/letter-grades` | Boundary values | Asked for tests exactly on each boundary (75 vs 74, etc.) | Parametrised test with 8 cases added; merged |
| `feature/ci-pipeline` | Does CI really prove the app runs? | Tests alone did not run the CLI | Added `compileall` build check and CLI smoke test; merged |
| `fix/empty-scores` | Error handling | `average([])` crashed with `ZeroDivisionError` | Clear `ValueError` plus test; merged |
| `feature/round-average` | Conflict with `fix/empty-scores` | Both branches edited `average()` | Conflict resolved by keeping both changes; both tests kept; merged |
| `chore/linting` | Style consistency | 2 lint errors, 2 unformatted files | All fixed; lint + format steps added to CI |
| `feature/class-summary` | Input validation | Summary accepted scores above 100 | Each score now validated; test added; merged |

> **Reviewer names and PR links:** replace this line with the GitHub PR numbers and the
> classmates who reviewed each one, e.g. `#4 – reviewed by @classmate`.

## 5. How to reproduce

```bash
pip install -r requirements-dev.txt
ruff check . && ruff format --check .
pytest --cov=gradebook --cov-report=term-missing
```

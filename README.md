# Student Gradebook

![CI](https://github.com/ADAGBON/student-gradebook/actions/workflows/ci.yml/badge.svg)

A small Python project used to introduce high school students to three core
software-engineering practices:

| Practice | Tool | Where to look |
|---|---|---|
| Version control | Git + GitHub | Commit history, branches, merged pull requests |
| Continuous integration | GitHub Actions | `.github/workflows/ci.yml`, the **Actions** tab |
| Quality assurance | pytest, ruff, code review | `tests/`, `pyproject.toml`, `QA_REPORT.md` |

## What the program does

```bash
python -m gradebook 70 85 92
# Average: 82.3 -> Grade A
```

`gradebook/grades.py` provides:

- `average(scores)` – mean rounded to 1 decimal place; rejects an empty list
- `validate_score(score)` – rejects scores outside 0–100
- `letter_grade(score)` – A (75+), B (65+), C (50+), D (40+), F
- `class_summary(scores)` – count, average, highest, lowest and pass rate

## Getting started

```bash
git clone https://github.com/ADAGBON/student-gradebook.git
cd student-gradebook
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

ruff check .        # lint
ruff format .       # auto-format
pytest --cov=gradebook   # run tests with coverage
```

## Student workflow (Part 1 – Git)

```bash
git switch main && git pull                 # 1. get the latest code
git switch -c feature/my-change             # 2. work in isolation on a branch
# ...edit code and tests...
git add -A && git commit -m "feat: ..."     # 3. stage and commit
git push -u origin feature/my-change        # 4. push and open a pull request
```

A pull request cannot be merged until CI is green and a classmate has reviewed it.

### Resolving a merge conflict

1. `git merge main` (or `git pull`) reports `CONFLICT` in a file.
2. Open the file and find the `<<<<<<<`, `=======`, `>>>>>>>` markers.
3. Decide what the final code should be (often a combination of both sides), delete the markers.
4. Run `pytest` to confirm both changes still work, then `git add <file>` and `git commit`.

This repo contains a real example: commit `Merge branch 'feature/round-average'`
combined the rounding change with the empty-list check from `fix/empty-scores`.

## CI pipeline (Part 2)

On every push and pull request, GitHub Actions runs, on Python 3.11 and 3.12:

1. **Lint** – `ruff check .`
2. **Format check** – `ruff format --check .`
3. **Build check** – `python -m compileall gradebook`
4. **Smoke test** – runs the command-line app
5. **Unit tests** – `pytest` with a 90% minimum coverage gate

A final `notify` job posts a pass/fail annotation on the run. GitHub also emails the
person who pushed when a run fails (Settings → Notifications → Actions).

## Project layout

```
.github/
  workflows/ci.yml             CI pipeline
  pull_request_template.md     review checklist for every PR
gradebook/
  grades.py                    grade logic
  __main__.py                  command-line entry point
tests/
  test_grades.py               unit tests for grades.py
  test_cli.py                  test for the command-line app
pyproject.toml                 ruff + pytest configuration
QA_REPORT.md                   tests, lint findings, code reviews
REFLECTION.md                  short reflection
```

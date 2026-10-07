"""Command-line entry point: python -m gradebook 70 85 92"""
import sys

from gradebook.grades import average, letter_grade


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    scores = [float(a) for a in args]
    mean = average(scores)
    print(f"Average: {mean} -> Grade {letter_grade(mean)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

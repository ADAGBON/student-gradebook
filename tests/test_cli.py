from gradebook.__main__ import main


def test_cli_prints_average_and_grade(capsys):
    assert main(["70", "80", "90"]) == 0
    assert capsys.readouterr().out.strip() == "Average: 80.0 -> Grade A"

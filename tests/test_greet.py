from ci_pipeline_test_upstream import USAGE, greet, main


def test_greet():
    assert greet("Ada") == "Hello, Ada."


def test_main_prints_the_greeting(capsys):
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada.\n"


def test_main_refuses_no_name(capsys):
    assert main([]) == 2
    assert capsys.readouterr().err.strip() == USAGE


def test_main_refuses_options(capsys):
    assert main(["--bogus"]) == 2
    assert capsys.readouterr().err.strip() == USAGE

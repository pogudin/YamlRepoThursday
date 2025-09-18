from goodhello import hello, bye

def test_hello_returns_none():
    assert hello() is None:

def test_bye_returns_none():
    assert bye() is None

def test_hello_prints_expected_test(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello DevOps!"

def test_bye_prints_expected_test(capsys):
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Good bye!"





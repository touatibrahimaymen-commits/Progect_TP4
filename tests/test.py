from src.Calculator import calculator

def test_empty_string():
    assert calculator("0") == 0

def test_empty_string_num():
    assert calculator("1") == 1
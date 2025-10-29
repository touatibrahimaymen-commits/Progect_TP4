from src.Calculator import calculator

def test_empty_string():
    assert calculator("0") == 0

def test_empty_string_num():
    assert calculator("1") == 1

def test_num_string_return_int():
    assert calculator("1,2") == 3

def test_num_string_return_int2():
    assert calculator("4,3") == 7

def test_num_string_return_int3():
    assert calculator("1,22") == 23
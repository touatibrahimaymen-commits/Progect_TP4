from src.Calculator import calculator
from src.Calculator import convert

def test_empty_string():
    assert calculator("0") == 0

def test_empty_string_num():
    assert calculator("1") == 1

def test_num_string_return_int():
    assert convert("1","2") == 3

def test_num_string_return_int2():
    assert convert("4","3") == 7

def test_num_string_return_int3():
    assert convert("1","22") == 23
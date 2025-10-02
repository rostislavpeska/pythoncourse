import pytest

def add_numbers(a:int, b:int) -> int:
    return a + b

# def test_foo():
#     x =2
#     y =2
#     assert x == y

def test_add_numbers():
    x = 1
    y = 2
    expected = 3
    result = add_numbers(x,y)
    assert result == expected

def divide_numbers (a: int,b: int) -> float:
    if b == 0:
        return 0
    else:
        return a/b

def test_divide_numbers():
    assert 1/1 == 1
    assert 10/2 == 5
    with pytest.raises(ZeroDivisionError):
        x= 10/0


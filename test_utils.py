from utils import add, subtract, multiply, divide, pow


def test_add():
    assert add(4, 8) == 12
    assert add(9, 5) == 14
    assert add(104, 1) == 105


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(19, 19) == 0
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(8, 4) == 32
    assert multiply(5, 9) == 45


def test_divide():
    assert divide(10, 2) == 5
    assert divide(18, 3) == 6
    assert divide(100, 5) == 20


def test_pow():
    assert pow(2, 2) == 4
    assert pow(4, 2) == 16
    assert pow(10, 2) == 100

import pytest


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def div(a, b):
    return a / b

@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 2, 3),
        (10, 2, 12),
        (10, -1, 9),
        (-1, -2, -3),
    ]
)
def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected, f"Ожидалось 2, получен {result}"

def test_multi():
    result = multiply(2, 6)
    assert result == 12

def test_divide():
    result = div(10, 2)
    assert result == 5

# def test_user(get_test_user):
#     assert get_test_user == "test"
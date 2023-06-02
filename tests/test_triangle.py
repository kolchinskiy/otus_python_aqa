import pytest


@pytest.fixture()
def fix():
    yield


@pytest.mark.parametrize('a, b, c', [(13, 14, 15)])
def test_triangle(fix, a, b, c):
    assert a > 0
    assert b > 0
    assert c > 0
    assert a + b > c
    assert a + c > b
    assert b + c > a
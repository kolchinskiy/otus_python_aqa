import pytest


@pytest.fixture()
def fix():
    yield


@pytest.mark.parametrize('a, b', [(10, 20)])
def test_triangle(fix, a, b):
    assert a > 0
    assert b > 0

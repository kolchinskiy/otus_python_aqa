import pytest


@pytest.fixture()
def fix():
    yield


@pytest.mark.parametrize('a', [10])
def test_triangle(fix, a):
    assert a > 0

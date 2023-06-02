import pytest


@pytest.fixture()
def fix():
    yield


@pytest.mark.parametrize('r', [10])
def test_triangle(fix, r):
    assert r > 0

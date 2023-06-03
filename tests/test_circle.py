import pytest
from python_aqa.src.circle import Circle


@pytest.mark.parametrize('r, exp_per, exp_area',
                         [
                             (10, 62.83, 314.16),
                             (2, 12.57, 12.57)
                         ]
                         )
def test_circle_positive(r, exp_per, exp_area):
    circle = Circle(r)
    assert circle.perimeter() == exp_per
    assert circle.area() == exp_area


@pytest.mark.parametrize('r',
                         [
                             -10,
                             0
                         ]
                         )
def test_circle_negative(r):
    with pytest.raises(ValueError):
        Circle(r)

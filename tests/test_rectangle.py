import pytest
from python_aqa.src.rectangle import Rectangle


@pytest.mark.parametrize('a, b, exp_per, exp_area',
                         [
                             (10, 20, 60, 200),
                             (2, 3, 10, 6)
                         ]
                         )
def test_rectangle_positive(a, b, exp_per, exp_area):
    rectangle = Rectangle(a, b)
    assert rectangle.perimeter() == exp_per
    assert rectangle.area() == exp_area


@pytest.mark.parametrize('a, b',
                         [
                             (10, -10),
                             (2, 0)
                         ]
                         )
def test_rectangle_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)
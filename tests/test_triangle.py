import pytest
from python_aqa.src.triangle import Triangle


@pytest.mark.parametrize('a, b, c, exp_per, exp_area',
                         [
                             (10, 10, 10, 30, 43.3),
                             (2, 2, 3, 7, 1.98),
                             (5, 6, 8, 19, 14.98)
                         ]
                         )
def test_triangle_positive(a, b, c, exp_per, exp_area):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter() == exp_per
    assert triangle.area() == exp_area


@pytest.mark.parametrize('a, b, c',
                         [
                             (10, 10, 0),
                             (2, 3, 17),
                             (-1, 2, 3)
                         ]
                         )
def test_triangle_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)

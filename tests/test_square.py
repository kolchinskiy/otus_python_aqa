import pytest
from python_aqa.src.square import Square


@pytest.mark.parametrize('a, exp_per, exp_area',
                         [
                             (10, 40, 100),
                             (2, 8, 4)
                         ]
                         )
def test_square_positive(a, exp_per, exp_area):
    square = Square(a)
    assert square.perimeter() == exp_per
    assert square.area() == exp_area


@pytest.mark.parametrize('a',
                         [
                             0,
                             -1
                         ]
                         )
def test_square_negative(a):
    with pytest.raises(ValueError):
        Square(a)
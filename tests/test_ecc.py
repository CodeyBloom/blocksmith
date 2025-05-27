import pytest

from ecc import FieldElement, Point


def test_field_add():
    a = FieldElement(7, 13)
    b = FieldElement(12, 13)
    c = FieldElement(6, 13)
    assert a + b == c


def test_field_sub():
    a = FieldElement(7, 13)
    b = FieldElement(12, 13)
    c = FieldElement(8, 13)
    assert a - b == c


def test_field_mul():
    a = FieldElement(3, 13)
    b = FieldElement(12, 13)
    c = FieldElement(10, 13)
    assert a * b == c


def test_field_pow():
    a = FieldElement(3, 13)
    b = FieldElement(1, 13)
    c = FieldElement(7, 13)
    d = FieldElement(8, 13)
    assert a**3 == b and c**-3 == d


def test_point_init():
    with pytest.raises(ValueError):
        Point(5, 7, -1, -2)


def test_point_inf():
    a = Point(5, 7, -1, -1)
    b = Point(5, 7, -1, 1)
    inf = Point(5, 7, None, None)
    assert a + b == inf
    assert b + a == inf
    assert a + inf == a
    assert inf + a == a
    assert inf + inf == inf
    assert b + inf == b


def test_on_curve():
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    valid_points = ((192, 105), (17, 56), (1, 193))
    invalid_points = ((200, 119), (42, 99))
    for x_raw, y_raw in valid_points:
        x = FieldElement(x_raw, prime)
        y = FieldElement(y_raw, prime)
        Point(a, b, x, y)
    for x_raw, y_raw in invalid_points:
        x = FieldElement(x_raw, prime)
        y = FieldElement(y_raw, prime)
        with pytest.raises(ValueError):
            Point(a, b, x, y)

@pytest.mark.parametrize("x1y1, x2y2, expected", [
def test_point_add(x1y1, x2y2, expected):
    prime = 223
    a = FieldElement(num=0, prime=prime)
    b = FieldElement(num=7, prime=prime)
    x1 = FieldElement(num=x1y1[0], prime=prime)
    y1 = FieldElement(num=x1y1[1], prime=prime)
    point1 = Point(a, b, x1, y1)
    x2 = FieldElement(num=x2y2[0], prime=prime)
    y2 = FieldElement(num=x2y2[1], prime=prime)
    point2 = Point(a, b, x2, y2)
    assert point1 + point2 == expected

from ecc import FieldElement


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

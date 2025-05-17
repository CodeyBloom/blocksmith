"""This module contains all the logic for doing elliptic curve cryptography (ECC) in python. This is basically my solutions
to the problems and exercises in the first few chapters of Programming Bitcoin"""

from dataclasses import dataclass
from typing import Type, TypeVar, cast

# Because I want type hints everywhere the dataclasses will be self referential. This helps with that.
FE = TypeVar("FE", bound="FieldElement")
PT = TypeVar("PT", bound="Point")


@dataclass(frozen=True)
class FieldElement:
    """A FieldElement is a member of a finite field of modulus prime."""

    num: int
    prime: int

    """Below is all the requisite operations required to satisfy a finite field. We use FE above to make it self-referring
    with the type hints. We use cast when returning to help with type hinting (this tells the interpreter to always cast to
    a field element of the same type). """

    def __post_init__(self: "FieldElement") -> None:
        """Validates the FieldElement is in the proper field range"""
        if self.num >= self.prime or self.num < 0:
            raise ValueError(f"Num {self.num} not in field range 0 to {self.prime - 1}")

    def __ne__(self, other: "FieldElement") -> bool:
        """Checks if two FieldElements are not equal."""
        if other is None:
            return False
        return not (self.num == other.num and self.prime == other.prime)

    def __add__(self, other: "FieldElement") -> FE:
        """Performs field-addition on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different Fields")
        num = (self.num + other.num) % self.prime
        return cast(Type[FE], self.__class__(num, self.prime))

    def __sub__(self, other: "FieldElement") -> FE:
        """Performs field-subtraction on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different Fields")
        num = (self.num - other.num) % self.prime
        return cast(Type[FE], self.__class__(num, self.prime))

    def __mul__(self, other: "FieldElement") -> FE:
        """Performs field-multiplication on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different Fields")
        num = (self.num * other.num) % self.prime
        return cast(Type[FE], self.__class__(num, self.prime))

    def __pow__(self: "FieldElement", exponent: int) -> FE:
        """Performs field-exponentiation on elements of a field order."""
        n = exponent % (self.prime - 1)  # in case exponent is negative
        num = pow(self.num, n, self.prime)
        return cast(Type[FE], self.__class__(num, self.prime))

    def __truediv__(self, other: "FieldElement") -> FE:
        """Performs field-division on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        # self/other = self * (other^-1) = self * (other^(prime-2)), thus we return:
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return cast(Type[FE], self.__class__(num, self.prime))


@dataclass(frozen=True)
class Point:
    """A Point is a point in the elliptic curve y^2=x^3+ax+b. This will be populated with FielElements in ECC."""

    a: FieldElement
    b: FieldElement
    x: FieldElement | None
    y: FieldElement | None # If x, y = None, this is the point at infinity (see __add__)

    def __post_init__(self: "Point") -> None:
        """Validates the Point is on the curve."""
        a = self.a
        b = self.b
        x = self.x
        y = self.y
        if self.x is None and self.y is None:
            return # To do addition on Points we need a point at infinity, this allows such a point to be created.
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError("({}, {}) is not on the curve".format(x, y))

    def __ne__(self, other: "Point") -> bool:
        """Checks if two Points are not equal."""
        if other is None:
            return False
        return not (self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b)

    def __add__(self, other: "Point") -> PT:
        """Performs point-addition on two points."""
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))

        # Additive identity cases where one (or both) of the points is the point at infinity:
        if self.x is None:
            return other
        if other.x is None:
            return self

        # Additive inverse case where the two points form a vertical line:
        if self.x == other.x and self.y != other.y:
            return cast(Type[PT], self.__class__(self.a, self.b, None, None))

        # Case where the two points are identical, (handling the possibility of the tangent line being vertical first):
        if self == other:
            if self.y.num == 0:
                return cast(Type[PT], self.__class__(self.a, self.b, None, None))
            else:
                lam = (3 * self.x**2 + self.a) / (2 * self.y)
                x3 = lam**2 - 2 * self.x
                y3 = lam * (self.x - x3) - self.y
                return cast(Type[PT], self.__class__(self.a, self.b, x3, y3))


        # Finally, the case where the two points are not inverse or identical:
        if self.x != other.x:
            # see page 35 in Programming Bitcoin for a proof
            lam = (other.y - self.y) / (other.x - self.x)
            x3 = lam**2 - self.x - other.x
            y3 = lam * (self.x - x3) - self.y
            return cast(Type[PT], self.__class__(self.a, self.b, x3, y3))

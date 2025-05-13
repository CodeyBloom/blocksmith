from dataclasses import dataclass
from typing import Type, TypeVar, cast

# Because I want type hints everywhere the FieldEleement dataclass will be self referential. This helps with that.
FE = TypeVar("FE", bound="FieldElement")


@dataclass(frozen=True)
class FieldElement:
    num: int
    prime: int

    """Below is all the requisite operations required to satisfy a field order. We use FE above to make it self-referring
    with the type hints. We use cast when returning to help with type hinting (this tells the interpreter to always cast to
    a field element of the same type). """

    def __post_init__(self) -> None:
        """Validates the FieldElement is in the proper field range"""
        if self.num >= self.prime or self.num < 0:
            raise ValueError(f"Num {self.num} not in field range 0 to {self.prime - 1}")

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
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return cast(Type[FE], self.__class__(num, self.prime))

    def __truediv__(self, other: "FieldElement") -> FE:
        """Performs field-division on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return cast(Type[FE], self.__class__(num, self.prime))


def main():
    print("Hello from blocksmith!")


if __name__ == "__main__":
    main()

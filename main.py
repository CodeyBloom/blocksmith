from dataclasses import dataclass


@dataclass(frozen=True)
class FieldElement:
    num: int
    prime: int

    def __post_init__(self) -> None:
        """Validates the FieldElement is in the proper field range"""
        if self.num >= self.prime or self.num < 0:
            raise ValueError(f"Num {self.num} not in field range 0 to {self.prime - 1}")

    def __add__(self, other):
        """Performs field-addition on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different Fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        """Performs field-subtraction on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different Fields")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        """Performs field-multiplication on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different Fields")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        """Performs field-exponentiation on elements of the same field order."""
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        """Performs field-division on elements of the same field order."""
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)


def main():
    print("Hello from blocksmith!")


if __name__ == "__main__":
    main()

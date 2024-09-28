# access control
from . import convert, fibonacci, generators, geometry, const, percentages, physics, probability


__all__ = ["const", "convert", "generators", "geometry", "percentages", "physics", "probability",
           "root", "simplify_fraction", "rule_of_3", "is_even", "is_odd", "is_prime", "is_div_by"]


def root(base: int | float, root: int|float = 2) -> int|float:
    """Calculate the root of the base.
    Example:
    > root(9, 2)
    This returns the square root of 9 (3)"""
    return base ** (1/root)


def simplify_fraction(numerator: int, denominator: int) -> tuple:
    """Simplifies a fraction of "numerator"/"denominator".
    Example:
    > simplify_fraction(12, 16)
    This return a tuple that is equal to (3, 4)."""

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    gcd = gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def rule_of_3(a1: int|float, b1: int|float, a2: int|float) -> int|float:
    """Finds the x in a rule of a rule of 3.
        Example:
        > rule_of_3(4, 2, 100)
        This returns 50.
        Explanation:
             4  - 2
            100 - x
            x = (2 * 100) / 4"""
    return (b1 * a2) / a1


def is_even(num: int) -> bool:
    """Checks if the variable "num" is even."""
    if num % 2 == 0:
        return True
    return False


def is_odd(num: int) -> bool:
    """Checks if the variable "num" is odd."""
    if is_even(num):
        return False
    return True


def is_div_by(num: int, divisor: int) -> bool:
    """Checks if the variable "num" is divisible by the variable "divisor"."""
    if num % divisor == 0:
        return True
    return False


def is_prime(num: int) -> bool:
    """Checks if the variable "num" is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

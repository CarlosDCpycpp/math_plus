import math

import collections.abc as c
import typing as t


def is_even(num) -> bool:
    """Checks if the variable "num" is even."""
    if num % 2 == 0:
        return True
    return False


def is_odd(num) -> bool:
    """Checks if the variable "num" is odd."""
    if is_even(num):
        return False
    return True


def is_div_by(num, divisor) -> bool:
    """Checks if the variable "num" is divisible by the variable "divisor"."""
    if num % divisor == 0:
        return True
    return False


def max_divisor(*args) -> int or None:
    """Finds the maximum common divisor of the *args."""
    def asd(a, b):
        while b:
            a, b = b, a % b
        return a
    if len(args) < 2:
        return None
    common_div = asd(args[0], args[1])
    for num in args[2:]:
        common_div = asd(common_div, num)
    return common_div


def is_prime(num) -> bool:
    """Checks if the variable "num" is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def root(base, root):
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
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def rule_of_3(a1, b1, a2):
    """Finds the x in a rule of a rule of 3.
    Example:
    > rule_of_3(4, 2, 100)
    This returns 50.
    Explanation:
         4  - 2
        100 - x
        x = (2 * 100) / 4"""
    return (b1 * a2) / a1


def bubble_sort(list_: list[int], biggest_lowest: bool = False) -> list:
    """Return a sorted version of the list that is given as an argument.
    By default, it sorts from lowest to biggest.
    If the argument "biggest_lowest" is true, it sorts from biggest to lowest."""
    lst = list_.copy()
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if biggest_lowest:
                if lst[j] < lst[j+1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                if lst[j] > lst[j+1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == "__main__":
    x = rule_of_3(4, 2, 100)
    print(x)

import string as _string

import collections.abc as _c

from .fibonacci import fib_gen as fibonacci_gen  # for access


def basic_gen(start: int = 1) -> _c.Generator:
    i = start
    while True:
        yield i
        i += 1


def prime_gen() -> _c.Generator:
    """Each call generates the next prime number."""
    num = 2
    while True:
        primes = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if primes:
            yield num
        num += 1


def root_gen(root: int, start: int = 1) -> _c.Generator:
    """Returns the x root of the consecutive integers (starting from the "start" variable, which, by default, is 0)."""
    n = start
    while True:
        yield n**(1/root)
        n += 1


def countdown_gen(start: int) -> _c.Generator:
    """Each call return the last call's return minus 1, the first call returns the start."""
    while start >= 0:
        yield start
        start -= 1


def power_gen(exponent: int) -> _c.Generator:
    """Generates the x power of consecutive integers."""
    n = 1
    while True:
        yield n**exponent
        n += 1


def alphabet_gen(lower: bool = False) -> _c.Generator:
    """Each call generates the next letter of the alphabet.
    If the "lower" variable is true (by default, is false), instead of uppercase letters
    the generator returns lowercase letters"""
    if lower:
        x = _string.ascii_lowercase
    else:
        x = _string.ascii_uppercase

    for lt in x:
        yield lt


def collatz_gen(num: int):
    """Generates the collatz sequence starting from the "num" variable (including)."""
    while num != 1:
        yield num
        if num%2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    yield 1

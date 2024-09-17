import random
import string

import collections.abc as c

import math_n_stuff as mns


def fibonacci_gen() -> c.Generator:
    """Each call returns the next element of the fibonacci sequence.
    Starting at 0."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_gen() -> c.Generator:
    """Each call generates the next prime number."""
    num = 2
    while True:
        primes = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if primes:
            yield num
        num += 1


def root_gen(root: int, start: int = 1) -> c.Generator:
    """Returns the x root of the consecutive integers (starting from the "start" variable, which, by default, is 0)."""
    n = start
    while True:
        yield n**(1/root)
        n += 1


def rng_gen(min=0, max=100) -> c.Generator:
    """Each call generates a random integer."""
    while True:
        yield random.randint(min, max)


def countdown_gen(start: int) -> c.Generator:
    """Each call return the last call's return minus 1, the first call returns the start."""
    while start >= 0:
        yield start
        start -= 1


def power_gen(exponent: int) -> c.Generator:
    """Generates the x power of consecutive integers."""
    n = 1
    while True:
        yield n**exponent
        n += 1


def alphabet_gen(lower: bool = False) -> c.Generator:
    """Each call generates the next letter of the alphabet.
    If the "lower" variable is true (by default, is false), instead of uppercase letters
    the generator returns lowercase letters"""
    if lower:
        x = string.ascii_lowercase
    else:
        x = string.ascii_uppercase

    for lt in x:
        yield lt


def collatz_gen(num: int):
    """Generates the collatz sequence starting from the "num" variable (including)."""
    while num != 1:
        yield num
        if mns.is_even(num):
            num //= 2
        else:
            num = 3 * num + 1
    yield 1


if __name__ == "__main__":
    gen = fibonacci_gen()

    switch: bool = True

    if switch:
        i = 1
        while i <= 100:
            nx = next(gen)
            print(nx)
            i += 1

    else:
        for nx in gen:
            print(nx)

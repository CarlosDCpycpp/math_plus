import collections.abc as _c

def fib_gen() -> _c.Generator:
    """Each call returns the next element of the fibonacci sequence.
    Starting at 0."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n: int = 10, include_zero: bool = True) -> list:
    fibonacci = []
    x = fib_gen()
    for _ in range(n):
        fibonacci.append(next(x))
    if not include_zero:
        fibonacci.remove(0)
        fibonacci.append(next(x))
    return fibonacci


def fib_element(n: int, include_zero: bool = True) -> int:
    x = fib(n, include_zero)
    return x[-1]


def fib_primes(n: int) -> list:
    def _is_prime(num) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = fib(n)
    z = []
    for i in x:
        if _is_prime(i):
            z.append(i)
    return z


def is_in_fib(n: int) -> bool:
    x = fib_gen()
    while True:
        i = next(x)
        if i == n:
            return True
        elif i > n:
            return False

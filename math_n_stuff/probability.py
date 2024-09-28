import math as _math


def simple_prob(favourable, total):
    return favourable / total


def combinations(total, chosen):
    return _math.factorial(total) // (_math.factorial(chosen) * _math.factorial(total - chosen))


def permutation(total, chosen):
    return _math.factorial(total) // _math.factorial(total - chosen)

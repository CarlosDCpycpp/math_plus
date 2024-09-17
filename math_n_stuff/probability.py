import math


def simple_prob(favourable, total):
    return favourable / total


def combinations(total, chosen):
    return math.factorial(total) // (math.factorial(chosen) * math.factorial(total - chosen))


def permutation(total, chosen):
    return math.factorial(total) // math.factorial(total - chosen)


if __name__ == "__main__":
    sp = simple_prob(1, 6)
    print(sp)

    c = combinations(6, 3)
    print(c)

    p = permutation(6, 3)
    print(p)

from math_n_stuff import rule_of_3


def find_perc(fraction: int | float, whole: int | float) -> int | float:
    return rule_of_3(whole, fraction, 100)


def find_increase(new_value: int | float, original_value: int | float) -> int | float:
    increase = new_value - original_value
    percentage_increase = find_perc(original_value, increase)
    return round(percentage_increase, 2)


def fraction_to_perc(numerator, denominator):
    return find_perc(denominator, numerator)


if __name__ == "__main__":
    z = find_increase(4, 2)
    print(z)


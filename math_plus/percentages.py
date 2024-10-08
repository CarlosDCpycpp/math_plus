from .utils import _rule_of_3_duplicate as _rule_of_3


def find_perc(fraction: int | float, whole: int | float) -> int | float:
    """Return the percentage of the fraction in relation to the whole (both are passed as arguments)"""
    return _rule_of_3(whole, fraction, 100)


def find_increase(new_value: int | float, original_value: int | float) -> int | float:
    """Return the percentage increase between 2 values that are passed as arguments."""
    increase = new_value - original_value
    percentage_increase = find_perc(original_value, increase)
    return round(percentage_increase, 2)


def fraction_to_perc(numerator, denominator):
    """Converts a fraction to percentage.
    This is done by taking the denominator as the whole and the numerator as the fraction."""
    return find_perc(denominator, numerator)

"""Program 26: Add list elements using a loop."""


def sum_of_list(numbers):
    """Return the total; an empty list returns zero."""
    total = 0
    for number in numbers:
        total += number
    return total

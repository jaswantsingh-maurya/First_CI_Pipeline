"""Program 25: Find maximum and minimum with a loop."""


def find_max_min(numbers):
    """Return (maximum, minimum); an empty list raises ValueError."""
    if not numbers:
        raise ValueError("Cannot find maximum and minimum of an empty list")
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum

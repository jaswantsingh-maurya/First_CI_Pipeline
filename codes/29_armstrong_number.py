"""Program 29: Check whether a number is an Armstrong number."""


def is_armstrong(number):
    """Compare the number with the total of its digits raised to its digit count."""
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == number

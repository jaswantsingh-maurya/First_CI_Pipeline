"""Program 30: Convert a nonnegative integer to binary by repeated division."""


def decimal_to_binary(number):
    """Return binary digits as a string; reject negative numbers."""
    if number < 0:
        raise ValueError("Binary conversion requires a nonnegative number")
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2
    return binary

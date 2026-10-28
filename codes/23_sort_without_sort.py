"""Program 23: Sort a copy of a list using bubble sort."""


def bubble_sort(numbers):
    """Return a new ascending list without changing the input."""
    result = list(numbers)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result

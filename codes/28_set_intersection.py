"""Program 28: Find elements common to two sets."""


def set_intersection(first, second):
    """Return a new set containing only elements present in both inputs."""
    common = set()
    for item in first:
        if item in second:
            common.add(item)
    return common

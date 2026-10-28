"""Program 27: Rotate a list to the right by k positions."""


def rotate_list(items, k):
    """Return a new list; negative k rotates left and empty input stays empty."""
    if not items:
        return []
    positions = k % len(items)
    if positions == 0:
        return list(items)
    return items[-positions:] + items[:-positions]

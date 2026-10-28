"""Program 24: Merge two already sorted lists."""


def merge_sorted_lists(list1, list2):
    """Return all elements in ascending order without changing either input."""
    merged = []
    first_index = 0
    second_index = 0
    while first_index < len(list1) and second_index < len(list2):
        if list1[first_index] <= list2[second_index]:
            merged.append(list1[first_index])
            first_index += 1
        else:
            merged.append(list2[second_index])
            second_index += 1
    merged.extend(list1[first_index:])
    merged.extend(list2[second_index:])
    return merged

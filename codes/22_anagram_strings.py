"""Program 22: Compare anagrams ignoring case and spaces."""


def is_anagram(first, second):
    """Return whether both strings contain the same character counts."""
    first_counts = {}
    second_counts = {}
    for letter in first.lower().replace(" ", ""):
        first_counts[letter] = first_counts.get(letter, 0) + 1
    for letter in second.lower().replace(" ", ""):
        second_counts[letter] = second_counts.get(letter, 0) + 1
    return first_counts == second_counts

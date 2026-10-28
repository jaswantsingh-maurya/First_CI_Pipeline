"""Program 21: Find the largest (longest) word in a sentence."""

import string


def largest_word(sentence):
    """Ignore surrounding punctuation; keep the first word in a tie."""
    largest = ""
    for word in sentence.split():
        clean = word.strip(string.punctuation)
        if len(clean) > len(largest):
            largest = clean
    return largest


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Largest word:", largest_word(text))

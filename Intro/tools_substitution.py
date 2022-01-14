from math import log10
from collections import Counter
from source import bigrams, trigrams


# Count every char frequency in encrypted text
def count_chars(encrypted):
    # Create new dictionary with Counter tool
    frequency_dict = Counter(encrypted)

    # Count frequencies
    frequency_dict = {char: round(n / len(encrypted), 10)
                      for char, n in sorted(frequency_dict.items(),
                                            key=lambda x: x[-1],
                                            reverse=True)}

    # Print result
    print(f'{len(frequency_dict) = }')
    print(f'{frequency_dict = }')


def reformat_dict(dictionary):
    total = sum(dictionary.values())
    for x, y in dictionary.items():
        dictionary[x] = log10(y / total)
    return dictionary

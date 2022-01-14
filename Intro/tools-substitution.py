from collections import Counter


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

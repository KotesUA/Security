from random import choice, choices, randint
from string import ascii_letters, digits
import os


def read_file(filename):
    with open(filename, "r") as f:
        return tuple(x.rstrip("\n") for x in f.readlines())


SOURCE_DIRECTORY = "data"
TOP100 = read_file(os.path.join(SOURCE_DIRECTORY, "top100.txt"))
TOP100K = read_file(os.path.join(SOURCE_DIRECTORY, "top100k.txt"))
WORDS = read_file(os.path.join(SOURCE_DIRECTORY, "words.txt"))
BASE = ascii_letters + digits


def top100_picker():
    return choice(TOP100)

def top100k_picker():
    return choice(TOP100K)


def random_generator():
    return "".join(choices(BASE, k=randint(10, 20)))


def humanlike_generator():
    words = []
    total_char_count, desired_char_count = 0, randint(8, 12)

    while total_char_count < desired_char_count:
        word = choice(WORDS)
        words.append(word)
        total_char_count += len(word)

    f = choice((str.lower, str.upper, str.capitalize))
    words = list(map(f, words))

    option = randint(1, 4)
    if option == 1:
        words.append(str(randint(0, 999)))
    elif option == 2:
        words.append(str(1970 + randint(0, 30)))
    
    return "".join(words)
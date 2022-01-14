import string
from math import log10
from collections import Counter
from random import random, sample, choice, randint


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


def readd_ngr4():
    with open('ngrams4.txt') as file:
        lines = file.readlines()
        ngr4 = {}
        for line in lines:
            l = line.split()
            ngr4[l[0]] = l[1]
        file.close()
    return ngr4


def random_gene():
    return Gene(''.join(choice(string.ascii_uppercase) for x in range(26)))


# Class to representation our gen
class Gene:
    def __init__(self, data):
        # дата это строка которую нам удалось расшифровать
        self.data = data
        self.score = 0

    # crossover two parents to create two children
    def crossover(self, partner):
        child = Gene(self.data)

        array = set(self.data)

        for own_data, partner_data in zip(self.data, partner.data):
            is_good1 = own_data in array
            is_good2 = partner_data in array
            if is_good1 and is_good2:
                new_char = choice((own_data, partner_data))
            elif is_good1:
                new_char = own_data
            elif is_good2:
                new_char = partner_data
            else:
                array.pop()
            child.data.append(new_char)
            array.discard(new_char)
        return child

    # меняем две буквы в строке местами
    def mutation(self):
        a = randint(0, 25)
        b = randint(0, 25)
        self.data[a], self.data[b] = self.data[b], self.data[a]
        # for i in range(len(bitstring)):
        #     # check for a mutation
        #     if rand() < r_mut:
        #         # flip the bit
        #         bitstring[i] = 1 - bitstring[i]

    def get_score(self):
        return 0


# genetic algorithm
def genetic_algorithm(ciphertext, dictionary, gen_number):
    gens = []
    for i in range(gen_number):
        g = random_gene()
        gens.append(g)

    gens = sorted(gens, key=lambda g: g.score)[:gen_number / 2]
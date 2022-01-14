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


def random_genes(number):
    return [Gene(''.join(choice(string.ascii_uppercase) for x in range(26))) for _ in range(number)]


# class to represent a gene
class Gene:
    def __init__(self, data):
        # data stores ascii string
        self.data = data
        # score stores self data value
        self.score = 0

    # crossover two parents to create two children
    def crossover(self, partner):
        child = Gene(self.data)

        array = set(self.data)

        for own_data, partner_data in zip(self.data, partner.data):
            is_good1 = own_data in array
            is_good2 = partner_data in array

            new_char = choice((own_data, partner_data)) if is_good1 and is_good2 \
                else own_data if is_good1 \
                else partner_data if is_good2 else array.pop()

            child.data.append(new_char)
            array.discard(new_char)
        return child

    # change two letters visa-versa
    def mutation(self):
        a = randint(0, 25)
        b = randint(0, 25)
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def get_score(self):
        return 0


def substitution_crack(text):
    genes = random_genes(1000)
    genes = sorted(genes, key=lambda gene: gene.score)[:500]

    for g in genes:
        g.get_score()

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
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, objective(pop[0])
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]


def fitness()

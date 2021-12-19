import random


def readIn():
    with open("encrypted.txt") as text:
        result = text.readlines()
    return result


def saveDecoded():
    print()
    # do something


if __name__ == '__main__':
    inText = readIn()
    for i in range(20):
        print([chr(ord(a) ^ ord(b)) for a, b in zip(random.choice(inText), random.choice(inText))])
        i += 1
    # TODO save letters that are resolved and repeat
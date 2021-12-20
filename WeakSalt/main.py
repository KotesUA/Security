import random


def readIn():
    with open("encrypted.txt") as text:
        result = text.readlines()
    return result


def saveDecoded():
    print()
    # do something


def XOR(str1, str2):
    return [chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)]



if __name__ == '__main__':
    inText = readIn()
    for i in range(1, 18):
        print(XOR(inText[0], inText[i]))
        i += 1
    # TODO save letters that are resolved and repeat
    # TODO if XOR encrypted and key results in decrypted, maybe should do reverse to know the key
    # \x00 is space
    # Big thx to https://samwho.dev/blog/toying-with-cryptography-crib-dragging/
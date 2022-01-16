from random import randint, choice
from string import ascii_letters, digits
import hashlib


# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt
def get100():
    passwords = []
    with open('top100.txt') as file:
        for p in file.readlines():
            p = ''.join(p.split('\n'))
            passwords.append(p)
    return passwords


# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
def get1M():
    passwords = []
    with open('top1000000.txt') as file:
        for p in file.readlines():
            p = ''.join(p.split('\n'))
            passwords.append(p)
    return passwords


TOP100 = get100()
TOP1M = get1M()


def generate(num):
    passwords = []
    for _ in range(num):
        r = randint(1, 100)
        if r in range(1, 10):
            passwords.append(choice(TOP100))
        elif r in range(11, 95):
            passwords.append(choice(TOP1M))
        else:
            passwords.append(''.join([choice(ascii_letters+digits) for _ in range(randint(8, 16))]))
    return passwords


def pass_md5(passwords):
    hashes = []
    for p in passwords:
        hashes.append(hashlib.md5(bytes(p, encoding="ascii")))
    return hashes


if __name__ == '__main__':
    print(generate(100))

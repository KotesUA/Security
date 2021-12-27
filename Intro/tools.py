import base64
import binascii

try:
    from math import gcd
except ImportError:
    from fractions import gcd
from functools import reduce

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,. '


def binary_to_text(bits):
    # Initializing a binary string in the form of 0 and 1, with base of 2
    binary_int = int(bits, 2)

    # Getting the byte number, +7 ensures we will get number divisible to 8
    byte_number = binary_int.bit_length() + 7 // 8

    # Getting an array of bytes
    binary_array = binary_int.to_bytes(byte_number, "big")

    # Converting binary array into ASCII text
    b64 = base64.b64decode(binary_array)

    # Decoding to readable text
    text = b64.decode("utf-8")

    # Splitting to lines
    return text.split('\n')


def single_byte_xor(encrypted, key):
    # Turn hex input to chars
    encrypted = binascii.unhexlify(encrypted)

    # XOR every encrypted char with key char
    decrypted = "".join([chr(item ^ key) for item in encrypted])

    # Remove some garbage
    decrypted = decrypted.replace('\x00', ' ').replace('\x0e', '\n').replace('½', '"').replace('¼', '"').replace('Â',
                                                                                                                 '').replace(
        '', '')

    return decrypted


def xor1_crack(encrypted, mode):
    # Turn hex or string input to char ints
    if mode == 0:
        encrypted = binascii.unhexlify(encrypted)
    else:
        encrypted = base64.b64decode(encrypted)

    # Try 255 keys from all ascii to decrypt
    possible_keys = []
    local_max = 0
    for i in range(255):
        count = 0
        for item in encrypted:
            c = chr(item ^ i)
            if c in SYMBOLS: count += 1
        if count > local_max:
            local_max = count

    # Find most relevant keys
    for i in range(255):
        count = 0
        for item in encrypted:
            c = chr(item ^ i)
            if c in SYMBOLS: count += 1
        if (count >= local_max - 2):
            possible_keys.append(chr(i))
    return possible_keys


def ascii_to_int(text):
    # this returns an int values array for an ASCII string
    return [ord(character) for character in text]


def vigenere_xor(text, key):
    key_length = len(key)
    text = base64.b64decode(text)
    key = ascii_to_int(key)
    result = ''.join(chr(text[i] ^ key[i % key_length]) for i in range(len(text)))
    return result


# Use Moving Average to find good values of shift
def find_key_length(encrypted):
    good_shifts = []
    MA = 5
    sum = 0
    encrypted = base64.b64decode(encrypted)

    # Review all shifts up to 50
    for shift in range(1, 51):
        encrypted_shifted = encrypted[shift:] + encrypted[:shift]

        # Count coincidence
        count = 0
        for a, b in zip(encrypted, encrypted_shifted):
            if a == b:
                count += 1

        # If count is larger than 3*MA - it's a good shift
        # Thx to my trading experience
        if count > 3 * MA:
            good_shifts.append(shift)
        sum += count
        MA = sum / shift

    # Find GCD of good shifts to find the best
    best_shift = reduce(gcd, good_shifts)
    return best_shift


def xor2_crack(encrypted):
    key = "L0l"

    # Find key length
    key_length = find_key_length(encrypted)

    # Split encrypted string to key_length substrings
    items = [encrypted[x:x + 12] for x in range(0, len(encrypted), 12)]

    # Find a key char for every Nth element of substrings
    possible_keys = []
    for n in range(0, key_length):
        temp = ''.join([items[i][n] for i in range(0, len(items) - 1)])
        possible_keys.append(xor1_crack(temp, 1))
    print(possible_keys)

    decrypted = vigenere_xor(encrypted, key)
    return decrypted.split('\n')

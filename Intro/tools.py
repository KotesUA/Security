import base64
import binascii
try:
    from math import gcd
except ImportError:
    from fractions import gcd
from functools import reduce


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


def xor1_crack(encrypted, key):
    # Turn hex input to chars
    encrypted = binascii.unhexlify(encrypted)

    # Try 255 keys from all ascii to decrypt
    # for i in range(255):
    #     decrypted = "".join([chr(item ^ i) for item in encrypted])
    #     print(i, " || ", decrypted)

    # Key 23 seems to be the answer
    decrypted = "".join([chr(item ^ key) for item in encrypted])

    # Remove some garbage
    decrypted = decrypted.replace('\x00', ' ').replace('\x0e', '\n').replace('½', '"').replace('¼', '"').replace('Â', '').replace('', '')

    return decrypted


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

    key_length = find_key_length(encrypted)
    print(key_length)

    # decrypted = vigenere_xor(encrypted, key)
    # return decrypted

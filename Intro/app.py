import base64
from tools import binary_to_text, single_byte_xor, xor2_crack, count_chars
from source import BITS, XOR1, XOR2, SUBSTITUTION


if __name__ == '__main__':
    res1 = binary_to_text(BITS)
    for line in res1:
        print(line)

    res2 = single_byte_xor(XOR1, 23)
    print(res2)

    res3 = xor2_crack(XOR2)
    print(res3)

    count_chars(SUBSTITUTION)

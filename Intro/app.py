import base64
from tools import binary_to_text, xor1_crack, xor2_crack
from source import BITS, XOR1, XOR2


if __name__ == '__main__':
    res1 = binary_to_text(BITS)
    for line in res1:
        print(line)

    res2 = xor1_crack(XOR1, 23)
    print(res2)

    res3 = xor2_crack(XOR2)
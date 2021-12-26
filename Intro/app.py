import base64
from tools import binary_to_text
from source import BITS


if __name__ == '__main__':
    res1 = binary_to_text(BITS)
    for line in res1:
        print(line)
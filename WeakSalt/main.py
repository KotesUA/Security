def readIn():
    with open("encrypted.txt") as text:
        result = [bytearray.fromhex(line) for line in text.readlines()]
        # result = text.readlines()
    return result


def XOR(str1, str2):
    res = [a ^ b for a, b in zip(str1, str2)]
    return res
    # return ([chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)])


def toHex(str):
    return bytearray.fromhex(''.join(hex(ord(s))[2:] for s in str))



if __name__ == '__main__':
    inText = readIn()
    zeroLine = "For who would bear the whips and scorns of time,".encode('utf-8').hex()

    print(inText[0])
    print(bytearray.fromhex(zeroLine))

    smth = XOR(inText[0], toHex(zeroLine))
    print(smth)

    text = ''
    for item in smth:
        text += chr(item)
    print(text)
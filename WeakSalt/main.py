# read encrypted file to bytearrays array line by line
def readIn():
    with open("encrypted.txt") as text:
        result = [bytearray.fromhex(line) for line in text.readlines()]
    return result


# XOR two bytearrays to a bytearray
def XOR(str1, str2):
    res = [a ^ b for a, b in zip(str1, str2)]
    return res


# convert bytearray to ASCII readable text
def toReadableText(arr):
    return ''.join([chr(item) for item in arr])


# convert ASCII string to bytearray
def toByteArray(str):
    return bytearray.fromhex(str.encode('utf-8').hex())


if __name__ == '__main__':
    inText = readIn()

    # XOR first string with every other and XOR with guessed words
    # for i in range(1, len(inText) - 1):
    #     res = XOR(inText[0], inText[i])
    #     line0 = XOR(res, toByteArray("Than fly to "))
    #     print(toReadableText(line0))

    # # XOR third line and decrypted line to recover the key
    key = XOR(inText[2], toByteArray("the pangs of dispriz'd love, the law's delay,"))

    # recover all ines and write to output
    with open("decrypted.txt", "a") as file:
        decrypted = [toReadableText(XOR(key, line)) for line in inText]
        print(decrypted)
        # file.writelines("\n".join(decrypted))
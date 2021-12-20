def XOR(str1, str2):
    return [a ^ b for a, b in zip(str1, str2)]


if __name__ == '__main__':
    key = "Fat rat eats cat"
    message = "Fat cat eats rat"
    encrypted = XOR(bytes.fromhex(key.encode('utf-8').hex()),
                    bytes.fromhex(message.encode('utf-8').hex()))
    print([item.hex() for item in encrypted])
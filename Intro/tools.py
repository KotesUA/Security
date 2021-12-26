import base64


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



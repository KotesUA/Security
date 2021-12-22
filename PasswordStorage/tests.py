from nacl import hash, encoding


def toBytes(str):
    return str.encode("utf-8")


def fromBytes(bytes):
    return bytes.decode("utf-8")


text = "Some string"
print(hash.sha512(toBytes(text), encoding.Base64Encoder))
print(hash.sha512(toBytes(text), encoding.Base64Encoder))
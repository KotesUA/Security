from nacl import hash, encoding
import secrets
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


KEK = b'\x8d\xcfR\xda\x83\xe2\xa06fp\xa2n\xadS\xdc\xd7\xb8\x02\xe7F\x08h\t\xe6\xd1\xda\x97i\xec4x\x97'


def to_bytes(text):
    return text.encode("utf-8")


def from_bytes(text):
    return text.decode("utf-8")


def gen_hash(text):
    return hash.sha512(to_bytes(text), encoding.Base64Encoder)


def gen_dek():
    dek_nonce = secrets.token_bytes(12)
    DEK = ChaCha20Poly1305.generate_key()
    return dek_nonce, DEK


def encrypt(nonce, text):
    # TODO
    print()


def decrypt(nonce, data):
    # TODO
    print()
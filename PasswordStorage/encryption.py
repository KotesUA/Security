from nacl import hash, encoding
import secrets
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


def to_bytes(text):
    return text.encode("utf-8")


def from_bytes(text):
    return text.decode("utf-8")


def gen_hash(text):
    return hash.sha512(to_bytes(text), encoding.Base64Encoder)


def gen_dek():
    dek = ChaCha20Poly1305.generate_key()
    return dek


def encrypt(key, text):
    nonce = secrets.token_bytes(12)
    return nonce, ChaCha20Poly1305(key).encrypt(nonce, text, None)


def decrypt(key, nonce, data):
    return ChaCha20Poly1305(key).decrypt(nonce, data, None)

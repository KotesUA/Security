import secrets
from datetime import datetime

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from nacl import hash
from OpenSSL import crypto, SSL


CERT_FILE = "selfsigned.crt"
KEY_FILE = "private.key"
PASS_FILE = "pass.bin"


def gen_key():
        return rsa.generate_private_key(65537, 2048, None)


def gen_pass():
        return secrets.token_bytes(32)


def gen_cert(key):
        subject = issuer = x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, "UA"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Kyiv"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "KPI"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Hotel California"),
                x509.NameAttribute(NameOID.COMMON_NAME, "laba.com"),
        ])

        now = datetime.datetime.utcnow()

        return (x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(issuer)
                .public_key(key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(now)
                .not_valid_after(now + datetime.timedelta(days=365))
                .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False,)
                .sign(key, hash.sha256()))


def setup():
        cert = gen_cert()
        key = gen_key()
        passphrase = gen_pass()

        with open(CERT_FILE, "wb") as file:
                file.write(cert.public_bytes(serialization.Encoding.PEM))

        with open(PASS_FILE, "wb") as file:
                file.write(passphrase)

        with open(KEY_FILE, "wb") as file:
                file.write(key.private_bytes(serialization.Encoding.PEM,
                                             serialization.PrivateFormat.TraditionalOpenSSL,
                                             serialization.BestAvailableEncryption(passphrase)))

        return CERT_FILE, KEY_FILE, PASS_FILE

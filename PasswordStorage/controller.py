from encryption import to_bytes, from_bytes, gen_hash, gen_dek, encrypt
import secrets
import sqlite3
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


KEK = b'\x8d\xcfR\xda\x83\xe2\xa06fp\xa2n\xadS\xdc\xd7\xb8\x02\xe7F\x08h\t\xe6\xd1\xda\x97i\xec4x\x97'


def register(email, password, number):
    create_users()
    connection = sqlite3.connect('database')
    cursor = connection.cursor()

    dek_nonce, DEK = gen_dek()
    encrypted_dek = ChaCha20Poly1305(KEK).encrypt(dek_nonce, DEK, None)
    nonce = secrets.token_bytes(12)

    encrypted_password = ChaCha20Poly1305(DEK).encrypt(nonce, gen_hash(password), None)
    encrypted_number = ChaCha20Poly1305(DEK).encrypt(nonce, to_bytes(number), None)
    cursor.execute("INSERT INTO users (email,password,number,dek,dek_nonce,nonce) VALUES (?,?,?,?,?,?)", (email,
                                                                                      encrypted_password,
                                                                                      encrypted_number,
                                                                                      encrypted_dek,
                                                                                      dek_nonce,
                                                                                      nonce))
    connection.commit()
    connection.close()


def login(email, password):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        record = cursor.fetchone()
        DEK = ChaCha20Poly1305(KEK).decrypt(record[5], record[4], None)
        result = gen_hash(password) == ChaCha20Poly1305(DEK).decrypt(record[6], record[2], None)
    except Exception:
        print(Exception)
        connection.commit()
        connection.close()
        return False
    connection.commit()
    connection.close()
    if not result:
        return result
    else:
        return ChaCha20Poly1305(DEK).decrypt(record[6], record[3], None)


def create_users():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email TEXT NOT NULL,password TEXT NOT NULL)")
    connection.commit()
    connection.close()


def show_users():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("SELECT email, password FROM users")
    users = cursor.fetchall()
    connection.close()
    return users


def drop_users():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    connection.commit()
    connection.close()

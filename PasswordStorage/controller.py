import sqlite3
from cryptography.fernet import Fernet


KEK = b'apT1vYBIu1ok9nniHAF6oWY-5aCN0rt9mkB6eedc6x4='


def toBytes(val):
    return bytes(val, encoding="utf-8")


def createUsers():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email TEXT NOT NULL,password TEXT NOT NULL)")
    connection.commit()
    connection.close()


def register(email, password, number):
    createUsers()
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    DEK = Fernet.generate_key()
    encrypted_password = Fernet(DEK).encrypt(toBytes(password))
    encrypted_number = Fernet(DEK).encrypt(toBytes(number))
    encrypted_dek = Fernet(KEK).encrypt(DEK)
    cursor.execute("INSERT INTO users (email,password,number,key) VALUES (?,?,?,?)", (email,
                                                                                      encrypted_password,
                                                                                      encrypted_number,
                                                                                      encrypted_dek))
    connection.commit()
    connection.close()


def login(email, password):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        record = cursor.fetchone()
        DEK = Fernet(KEK).decrypt(record[4])
        result = toBytes(password) == Fernet(DEK).decrypt(record[2])
    except Exception:
        connection.commit()
        connection.close()
        return False
    connection.commit()
    connection.close()
    if not result:
        return result
    else:
        return Fernet(DEK).decrypt(record[3])


def showUsers():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("SELECT email, password FROM users")
    users = cursor.fetchall()
    connection.close()
    return users


def dropUsers():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    connection.commit()
    connection.close()

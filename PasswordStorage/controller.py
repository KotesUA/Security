import sqlite3
from cryptography.fernet import Fernet


KEY = b'apT1vYBIu1ok9nniHAF6oWY-5aCN0rt9mkB6eedc6x4='
KEY_TEL = b'ulsiCWAvTfSA_SBb9gwfgAx4yI3aieqUShg5u4QNbQg='


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
    encrypted_password = Fernet(KEY).encrypt(toBytes(password))
    encrypted_number = Fernet(KEY_TEL).encrypt(toBytes(number))
    cursor.execute("INSERT INTO users (email,password,number) VALUES (?,?,?)", (email,encrypted_password,encrypted_number))
    connection.commit()
    connection.close()


def login(email, password):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        record = cursor.fetchone()
        result = toBytes(password) == Fernet(KEY).decrypt(record[2])
    except Exception:
        connection.commit()
        connection.close()
        return False
    connection.commit()
    connection.close()
    return Fernet(KEY_TEL).decrypt(record[3])


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

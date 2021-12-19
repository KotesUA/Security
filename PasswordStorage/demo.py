import sqlite3

from cryptography.fernet import Fernet


KEY = b'apT1vYBIu1ok9nniHAF6oWY-5aCN0rt9mkB6eedc6x4='


def toBytes(val):
    return bytes(val, encoding="utf-8")


connection = sqlite3.connect('database')
cursor = connection.cursor()
cursor.execute("SELECT * FROM users WHERE email = ?", ("mail@mail.com",))
record = cursor.fetchone()

print(Fernet(KEY).encrypt(toBytes("Pass2021")))
print(Fernet(KEY).decrypt(record[2]))
print(record[2])

result = toBytes("Pass2021") == Fernet(KEY).decrypt(record[2])
connection.commit()
connection.close()


print(result)
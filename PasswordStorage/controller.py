from encryption import *
import sqlite3


KEK = b'\x8d\xcfR\xda\x83\xe2\xa06fp\xa2n\xadS\xdc\xd7\xb8\x02\xe7F\x08h\t\xe6\xd1\xda\x97i\xec4x\x97'


def register(email, password, number):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()

    dek = gen_dek()
    print(dek)
    dek_nonce, encrypted_dek = encrypt(KEK, dek)

    pass_nonce, encrypted_password = encrypt(dek, gen_hash(password))
    num_nonce, encrypted_number = encrypt(dek, to_bytes(number))

    cursor.execute("INSERT INTO users (email,password,number,dek,dek_nonce,pass_nonce,num_nonce) VALUES (?,?,?,?,?,?,?)",
                   (email, encrypted_password, encrypted_number, encrypted_dek, dek_nonce, pass_nonce, num_nonce))
    connection.commit()
    connection.close()


def login(email, password):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    record = cursor.fetchone()
    dek = decrypt(KEK, record[5], record[4])
    result = gen_hash(password) == decrypt(dek, record[6], record[2])

    connection.commit()
    connection.close()
    if not result:
        return result
    else:
        return decrypt(dek, record[6], record[3])

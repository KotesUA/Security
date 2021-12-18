import sqlite3


def createUsers():
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email TEXT NOT NULL,password TEXT NOT NULL)")
    connection.commit()
    connection.close()


def register(email, password):
    createUsers()
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (email,password) VALUES (?,?)", (email, password))
    connection.commit()
    connection.close()


def login(email, password):
    connection = sqlite3.connect('database')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        record = cursor.fetchone()
        result = password == record[2]
    except Exception:
        connection.commit()
        connection.close()
        return False
    connection.commit()
    connection.close()
    return result


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

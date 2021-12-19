import sqlite3

from cryptography.fernet import Fernet


print(Fernet.generate_key())
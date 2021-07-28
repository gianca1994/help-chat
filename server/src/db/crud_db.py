import sqlite3
from sqlite3.dbapi2 import connect
from werkzeug.security import check_password_hash, generate_password_hash


def encrypt_password(password):
    return generate_password_hash(password=password)


def validate_password(encrypt_password, password):
    return check_password_hash(encrypt_password, password)


def register_user(username, password):
    conn = connect(database="DataBase.db")

    try:

        cur = conn.cursor()
        password_encrypted = encrypt_password(password)

        cur.execute("INSERT INTO users (user_name, password, operator) "
                    f"VALUES ('{username}', '{password_encrypted}', False)")
        conn.commit()
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def login_user(username, password):
    conn = connect(database="DataBase.db")
    validate_user = False
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        for i in cur.fetchall():
            if i[1] == username:
                if validate_password(i[2], password):
                    validate_user = True
        return validate_user
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

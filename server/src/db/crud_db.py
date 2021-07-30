import sqlite3
from sqlite3.dbapi2 import connect
from werkzeug.security import check_password_hash, generate_password_hash
import logging


def encrypt_password(password):
    return generate_password_hash(password=password)


def validate_password(encrypted_password, password):
    return check_password_hash(encrypted_password, password)


def check_user_existence(username):
    conn = connect(database="DataBase.db")
    user_exist = False
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        for i in cur.fetchall():
            if i[1] == username:
                user_exist = True
        return user_exist
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def register_user(username, password, rol):
    conn = connect(database="DataBase.db")
    user_register = False
    try:
        cur = conn.cursor()
        password_encrypted = encrypt_password(password)
        if not check_user_existence(username=username):
            cur.execute("INSERT INTO users (user_name, password, operator) "
                        f"VALUES ('{username}', '{password_encrypted}', False)")
            conn.commit()
            logging.warning('<< REGISTER >> ' + ' USERNAME: ' + username + ' - ' + 'ROL: ' + rol)
            user_register = True

        return user_register
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def login_user(username, password, rol):
    conn = connect(database="DataBase.db")
    validate_user = False

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        for i in cur.fetchall():
            if i[1] == username:
                if validate_password(i[2], password):
                    validate_user = True
                    logging.warning('<< LOGIN >> ' + ' USERNAME: ' + username + ' - ' + 'ROL: ' + rol)
        return validate_user
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

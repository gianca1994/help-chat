import sqlite3
from sqlite3.dbapi2 import connect


def register_user(username, password):
    conn = connect(database="DataBase.db")

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (user_name, password, operator) "
                    f"VALUES ('{username}', '{password}', False)")
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
                if i[2] == password:
                    validate_user = True
        return validate_user
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

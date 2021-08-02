import sqlite3
from sqlite3.dbapi2 import connect


def make_tables():
    conn = connect(database="DataBase.db")

    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE users(id integer PRIMARY KEY, user_name text, password text, operator boolean)")
        # cur.execute("CREATE TABLE rooms(id integer PRIMARY KEY, operator text, client text, active boolean)")
        conn.commit()
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

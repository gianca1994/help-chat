import sqlite3
from sqlite3.dbapi2 import connect


def make_tables():
    """
    Function used to create the user table.

    :return:
        none
    """

    conn = connect(database="DataBase.db")

    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE users(id integer PRIMARY KEY, user_name text, password text, operator boolean)")
        conn.commit()
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

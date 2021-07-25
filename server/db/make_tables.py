import sqlite3
from sqlite3.dbapi2 import connect

tables = [
    "CREATE TABLE clients(id integer PRIMARY KEY, user_name text, password text, email text)",
    "CREATE TABLE operators(id integer PRIMARY KEY, zone_id int)",
    "CREATE TABLE rooms(id integer PRIMARY KEY, id_operator int, id_client int, id_zone int)",
    "CREATE TABLE zones(id integer PRIMARY KEY, name_zone text)"
]

zones = [
    'TECHNIQUE',
    'ADMINISTRATIVE',
    'SALES'
]


def make_tables():
    conn = connect(database="DataBase.db")

    try:
        cur = conn.cursor()

        for i in tables:
            cur.execute(i)

        for i in zones:
            cur.execute(f"INSERT INTO zones(name_zone) VALUES ('{i}')")

        conn.commit()

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

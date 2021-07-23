
import sqlite3
from sqlite3.dbapi2 import connect

def make_tables():
 
    conn = connect(database="DataBase.db")

    try:
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE clients(id integer PRIMARY KEY, user_name text, password text, email text)")
        cur.execute("CREATE TABLE operators(id integer PRIMARY KEY, name_operator text, zone_id int)")
        cur.execute("CREATE TABLE rooms(id integer PRIMARY KEY, id_operator int, id_client int, id_zone int)")
        cur.execute("CREATE TABLE zones(id integer PRIMARY KEY, name_zone text)")

        conn.commit()
        
    except sqlite3.OperationalError as error:
        print(error)
    conn.close()

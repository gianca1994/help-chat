import os
import sqlite3


def connect():
    """
    We execute the connection with the database, initializing the
    connection as 'None' and we set the PATH and the NAME of the database.
    """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join('server/', 'DataBase.db'))
    except OSError as e:
        print(e)
    return conn

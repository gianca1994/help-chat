import os

from src.db.make_tables import make_tables


def check_existence_db():
    """
    Function used to check if the database is in the root directory
    of the server, if it is not found, it creates it by calling the
    'make_tables' method.

    :return:
        none
    """

    if not os.path.isfile('DataBase.db'):
        make_tables()

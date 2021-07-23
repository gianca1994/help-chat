import os
from db.make_tables import make_tables

def check_existence_db():
    
    if not os.path.isfile('DataBase.db'):
        make_tables()
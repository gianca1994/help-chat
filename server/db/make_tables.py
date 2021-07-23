from connect import connect


conn = connect()


def client_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE clients(id integer PRIMARY KEY, user_name text, password text, email text)")
    conn.commit()

def operator_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE operators(id integer PRIMARY KEY, name_operator text, zone_id int)")
    conn.commit()
    
def room_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE rooms(id integer PRIMARY KEY, id_operator int, id_client int, id_zone int)")
    conn.commit()
    
def zone_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE zones(id integer PRIMARY KEY, name_zone text)")
    conn.commit()

client_table()
operator_table()
room_table()
zone_table()

conn.close()
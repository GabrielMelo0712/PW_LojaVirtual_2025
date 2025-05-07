import sqlite3

def get_conncetion():
    conn = None
    try:
        conn = sqlite3.connect("dados.db")
    except sqlite3.Error as e:
        print(e)
    return conn
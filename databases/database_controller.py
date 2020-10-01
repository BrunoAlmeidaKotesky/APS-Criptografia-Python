import sqlite3 as sql
from Crypto.Hash import MD4
from typing import  Union
import os.path

DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(DIR, 'testedb.db')

def md4Hash(text: str):
    h = MD4.new()
    try:
        h.update(bytes(text, encoding='utf-8'))
        return h.hexdigest()
    #Not now
    except: Exception

def connect_database(db=DB_NAME):
    if db is None:
        mydb = ':memory:'
    else:
        mydb = db
        print('Conexao Estabilizada')
    with sql.connect(db) as connection:
        connection.create_function("md4", 1, md4Hash)
        sql.enable_callback_tracebacks(True)
        return connection

def disconnect_from_db(db=None, conn=None):
    if db is not DB_NAME:
        print("You are trying to disconnect from a wrong DB")
    if conn is not None:
        conn.close()



from Crypto.Hash import MD4
import sqlite3 as sql
from typing import  Union

nome_user = input('Insira o nome do usuario: ')
sobrenome_user = input('Insira o sobrenome do usuario: ')
senha = input('Insira uma senha: ')

h = MD4.new()
# h.update(b'UmaSenhaMuitoSegura123cls')
# print(h.hexdigest())

connection = sql.connect('databases\\testedb.db')
sql.enable_callback_tracebacks(True)
def md4Hash(text: Union[bytes, bytearray, memoryview]):
    try:
        h.update(bytes(text, encoding='utf-8'))
        return h.hexdigest()
    except: raise Exception
connection.create_function("md4", 1, md4Hash)
c = connection.cursor()

c.execute("INSERT INTO usuarios VALUES(null, ?, ?, md4(?))", [nome_user, sobrenome_user, senha])
connection.commit()

c.execute("select senha from usuarios where nome_usuario='{nome_usuario}'".format(nome_usuario=nome_user))
nome = c.fetchone()
print('Senha criptografada do Usuário: ', nome[0])
c.close()
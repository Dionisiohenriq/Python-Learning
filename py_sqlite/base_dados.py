import sqlite3

connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 80.5))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'João',
#                 'peso': 60})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None,
#                 'nome': 'João',
#                 'peso': 60})
# connection.commit()
# sql = 'UPDATE clientes SET nome = ?, peso = ? WHERE id = ?'
# cursor.execute(sql, ('Roberto', 80, 4))
# connection.commit()
# cursor.execute('DELETE FROM clientes WHERE id = :id', {'id': 4})
# connection.commit()


cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 60})
for linha in cursor.fetchall(): # busca todos os resultados do cursor
    nome, peso = linha
    print(nome, peso)


print(cursor.rowcount, "record(s) affected")

cursor.close()
connection.close()
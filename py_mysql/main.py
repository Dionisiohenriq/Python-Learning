import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,

    )
    try:
        yield conn
    finally:
        conn.close()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES(%s, %s, %s, %s)"
#         cursor.execute(sql, ('Henrique', 'Ferreira', 31, 74))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES(%s, %s, %s, %s)"
#         dados = [
#             ('Muriel', 'Figueiredo', 15, 60),
#             ('Rose', 'Darling', 23, 60),
#             ('Jack', 'Ryan', 60, 80)
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id = %s"
#         cursor.execute(sql, (9,))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id IN(%s, %s, %s)"
#         cursor.execute(sql, (6, 7, 8))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id BETWEEN %s AND %s"
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "DELETE FROM clientes WHERE id IN(%s, %s, %s)"
#         cursor.execute(sql, (6, 7, 8))
#         conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome = %s WHERE id = %s'
        cursor.execute(sql, ('Ronaldo', 4))
        conexao.commit()
        print(cursor.rowcount, "record(s) affected.")



with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY ID DESC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

        print(cursor.rowcount, "record(s) affected.")
        print()



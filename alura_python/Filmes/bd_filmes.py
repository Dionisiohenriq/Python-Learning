import pymysql.cursors
from contextlib import contextmanager


class Bdfilmes():

    def __init__(self, list = []):
        self.list = list

    @contextmanager
    def conecta(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='Rique#2020',
            db='programas',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            port=3307
        )
        try:
            yield self.conn
        finally:
            self.conn.close()

    def cadastra(self):
        with self.conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'INSERT INTO filmes (nome, ano, duracao, likes) VALUES (%s, %s, %s, %s)'
                nome, ano, duracao, likes = self.list
                cursor.execute(sql, (nome, ano, duracao, likes))
                conexao.commit()

    def altera(self, nome, ano, duracao, likes):
        with self.conecta() as conexao:
            with conexao.cursor as cursor:
                sql = 'UPDATE filmes SET nome = %s, ano = %s, duracao = %s, likes = %s WHERE nome LIKE = %s'
                cursor.execute(sql, (nome, ano, duracao, likes, f'%{nome}%',))
                conexao.commit()

    def consulta(self, nome):
        with self.conecta() as conexao:
            with conexao.cursor as cursor:
                sql = 'SELECT * FROM filmes WHERE nome LIKE = %s'
                cursor.execute(sql, (nome,))
                conexao.commit()

    def exclui(self, nome, id):
        with self.conecta() as conexao:
            with conexao.cursor as cursor:
                sql = 'DELETE FROM filmes WHERE nome LIKE = %s AND id = %s'
                cursor.execute(sql, (nome, id))
                conexao.commit()
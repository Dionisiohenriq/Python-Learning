import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = "INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)"
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = "UPDATE OR IGNORE agenda SET nome = ?, telefone = ? WHERE id = ?"
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = "DELETE FROM agenda WHERE id = ?"
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, nome):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{nome}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Henrique', '1199695-6885')
    # agenda.inserir('Maria', '1196301-0926')
    # agenda.inserir('Teste', '1111111-1111')
    # agenda.inserir('Augusto', '1112343-1234')
    # agenda.inserir('Antonio', '112492-6352')
    # agenda.editar('Melissa', '1199695-6875', 5)
    agenda.listar()
    # agenda.listar()
    agenda.fechar()
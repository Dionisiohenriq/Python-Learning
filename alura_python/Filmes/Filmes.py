from Programas import Programa as prog
from playlist import Playlist

class Filme(prog):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao += nova_duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self.likes}'

    def adiciona_filme(self):
        """
        Função que pega novos filmes e os adiciona a uma nova Playlist
        """
        adicionar_filme = input("Insira títutlo, ano e duração em minutos, separados por vírgula, ou 0 para sair")

        lista_filmes = []

        while adicionar_filme != '0':

            adicionar_filme = adicionar_filme.strip().split(',')

            prog.nome = adicionar_filme[0]
            prog.ano = int(adicionar_filme[1])
            self.duracao = int(adicionar_filme[2])

            lista_filmes.append(Filme(prog.nome, prog.ano, self.duracao))

            adicionar_filme = input("Insira títutlo, ano e duração em minutos, separados por vírgula, ou 0 para sair\n")

        if lista_filmes != []:
            minha_playlist = Playlist('nova', lista_filmes)
            return minha_playlist
        else:
            return "\n**Fim da adição de Filmes**\n"




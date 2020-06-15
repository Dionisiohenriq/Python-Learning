from programas import Programa as prog
from playlist import Playlist
from bd_filmes import Bdfilmes


class Filme(prog):

    def __init__(self, nome, ano, duracao, likes):
        super().__init__(nome, ano)
        self.__duracao = duracao
        self.__likes = likes
        self._iteravel = nome, ano, duracao, likes

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self.likes}'

    def __getitem__(self, item):
        return self._iteravel[item]

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao += nova_duracao

    @staticmethod
    def adiciona_filme():
        """
        Função que pega novos filmes e os adiciona a uma nova Playlist
        """
        adicionar_filme = input("Insira títutlo, ano e duração em minutos, separados por vírgula, ou 0 para sair")

        lista_filmes = []

        while adicionar_filme != '0':

            adicionar_filme = adicionar_filme.strip().split(',')
            Bdfilmes.cadastra(adicionar_filme)

            prog.nome = adicionar_filme[0]
            prog.ano = int(adicionar_filme[1])
            duracao = int(adicionar_filme[2])
            likes = int(adicionar_filme[3])

            # add an object of Filme with every user entry to every position of lista_filmes
            lista_filmes.append(Filme(prog.nome, prog.ano, duracao, likes))

            adicionar_filme = input("Insira títutlo, ano e duração em minutos, separados por vírgula, ou 0 para sair\n")

        # if has values in lista_filmes, create an object of Playlist to minha_playlist
        if lista_filmes:
            minha_playlist = Playlist('nova', lista_filmes)
            return minha_playlist
        else:
            return "\n**Fim da adição de Filmes**\n"




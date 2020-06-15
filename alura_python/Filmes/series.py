from programas import Programa as prog
from playlist import Playlist

class Serie(prog):


    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    # Um @property é um método acessor ( GET )
    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, nova_qtd):
        self.__temporadas += nova_qtd

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} - {self.likes}'

    @staticmethod
    def adiciona_serie():
        """
        Função que pega novos filmes e os adiciona a uma playlist
        """
        adicionar_serie = input("Insira títutlo, ano e quantidade de temporadas, separados por vírgula, ou 0 para sair")

        lista_series = []

        while adicionar_serie != '0':

            adicionar_serie = adicionar_serie.strip().split(',')

            prog.nome = adicionar_serie[0]
            prog.ano = int(adicionar_serie[1])
            temporadas = int(adicionar_serie[2])

            lista_series.append(Serie(prog.nome, prog.ano, temporadas))

            adicionar_serie = input("Insira títutlo, ano e quantidade de temporadas, separados por vírgula, ou 0 para sair\n")

        if lista_series:
            minha_playlist = Playlist('nova', lista_series)
            return minha_playlist
        else:
            return "\n**Fim da adição de Séries**\n"


class Programa:

    _diretor = 'Steven'

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'
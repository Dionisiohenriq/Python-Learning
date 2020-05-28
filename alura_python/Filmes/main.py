from Filmes import Filme
from series import Serie
from playlist import Playlist


def main():

    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    got = Serie('game of thrones', 2018, 8)
    matrix = Filme('matrix', 1999, 150)
    twd = Serie('The walking Dead', 2015, 15)

    Filme.adiciona_filme()
    Serie.adiciona_serie()

    # ctrl + d duplica linhas, ctrl + shift + seta cima ou baixo, muda linhas de lugar
    got.dar_likes()
    got.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()
    matrix.dar_likes()
    matrix.dar_likes()
    matrix.dar_likes()
    twd.dar_likes()
    twd.dar_likes()
    twd.dar_likes()

    lista = [vingadores, got, matrix, twd]
    minha_playlist = Playlist('fds', lista)
    [print(programas) for programas in minha_playlist]
    print(len(minha_playlist))


if __name__ == '__main__':
    main()

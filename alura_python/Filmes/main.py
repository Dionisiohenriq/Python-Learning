from filmes import Filme
from series import Serie
from playlist import Playlist
from bd_filmes import Bdfilmes

def main():

    vingadores = Filme('vingadores - guerra infinita', 2018, 160, 20)
    #got = Serie('game of thrones', 2018, 8)
    matrix = Filme('matrix', 1999, 150, 20)
    #twd = Serie('The walking Dead', 2015, 15)

    Filme.adiciona_filme()
    Serie.adiciona_serie()

    # ctrl + d duplica linhas, ctrl + shift + seta cima ou baixo, muda linhas de lugar
    #got.dar_likes()
    #got.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()
    matrix.dar_likes()
    matrix.dar_likes()
    matrix.dar_likes()
    #twd.dar_likes()
    #twd.dar_likes()
    #twd.dar_likes()

    lista = [vingadores, matrix]
    minha_playlist = Playlist('fds', lista)
    # print(minha_playlist)
    # print(len(minha_playlist))
    # DaoFilmes()

    # bd_test = Bdfilmes(minha_playlist)
    # bd_test.cadastra()

if __name__ == '__main__':
    main()

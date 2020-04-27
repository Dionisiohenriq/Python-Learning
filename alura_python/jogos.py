import forca
import adivinhacao

def escolha_jogo():
    print(29 * "*")
    print("Bem vindo a escolha de jogos!")
    print(29 * "*")

    print("(1)Forca --- (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
        print("Jogando Adivinhação")


if __name__ == "__main__":
    escolha_jogo()
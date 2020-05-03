import random


def jogar():
    imprime_mensagem_abertura()

    # coletando os dados do arquivo para nosso jogo
    palavra_secreta = escolha_palavra()
    palavra = gera_palavra_secreta(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    # mostra a qtd de letras da palavra, como dica
    print(palavra)

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:

        chute = input("Insira uma letra").lower().strip()

        if chute in palavra_secreta:
            aponta_acertos(chute, palavra_secreta, palavra)
        else:
            erros += 1
            print(f"Faltam {7 - erros} tentativas.")
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in palavra
        print(palavra)
        print("Jogando...")

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo!")


def imprime_mensagem_abertura():
    print(27 * "*")
    print("Bem vindo ao jogo de forca!")
    print(27 * "*")


def escolha_palavra():
    with open('palavras.txt', 'a') as frutas:
        marcador = ""
        while marcador != "q":
            dicionario = input("Insira uma palavra ou digite 'q' para sair\n")
            marcador = dicionario
            if dicionario != 'q':
                frutas.write(f"{dicionario}\n")

    with open('palavras.txt', 'r') as frutas:
        escolha = frutas.readlines()
    escolha = [x.strip().lower() for x in escolha]
    escolha = random.choice(escolha)
    return escolha


def gera_palavra_secreta(palavra):
    palavra = ["_" for _ in palavra]
    return palavra


def aponta_acertos(chute, palavra_secreta, palavra):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            print(f"Letra {letra}, encontrada na posição: {index}")
            palavra[index] = chute
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if __name__ == "__main__":
    jogar()

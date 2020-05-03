import random as rd

def jogar():
    print(33 * "*")
    print("Bem vindo ao jogo de adivinhação!")
    print(33 * "*")

    numero_secreto = rd.randrange(1, 101)
    total_tentativas = 0
    nivel = 0
    pontuacao = 1000
    print("Defina um nível de dificuldade:",
          "Nível(1):Fácil Nível(2:Médio Nível(3):Difícil")

    while nivel not in range(1, 4):

        nivel = int(input("Insira o nível: "))

        if nivel == 1:
            total_tentativas = 20

        elif nivel == 2:
            total_tentativas = 10

        elif nivel == 3:
            total_tentativas = 5

        else:
            print("Nível inválido!")


    for rodada in range(1, total_tentativas + 1):

        print(f"Tentativa {rodada:02d} de {total_tentativas:02d}")
        chute_usuario = int(input("Insira um número: "))
        print("Você digitou: ", chute_usuario)

        if chute_usuario < 1 or chute_usuario > 100:
            print("Você digitou um valor entre 1 e 100!")
            continue

        acertou = (chute_usuario == numero_secreto)
        maior = (chute_usuario > numero_secreto)
        menor = (chute_usuario < numero_secreto)

        if acertou:
            print(f"Você acertou!")
            break
        else:
            if maior:
                print("Você errou! Seu chute foi maior que o número secreto!")
            elif menor:
                print("Você errou! Seu chute foi menor que o número secreto!")
            else:
                print("Número inválido!")
            pontos_perdidos = abs(numero_secreto - chute_usuario)
            pontuacao = pontuacao - pontos_perdidos
            if rodada == total_tentativas:
                print(f"O número secreto era {numero_secreto}, você fez {pontuacao} pontos.")

        chute_usuario = 0
        rodada += 1

    print(f"Fim do jogo! Sua pontuacao: {pontuacao}, número secreto: {numero_secreto}")


if __name__ == "__main__":
    jogar()
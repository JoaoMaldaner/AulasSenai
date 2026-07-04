def criar_tabuleiro():    #vai criar um tabuleiro
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro(tabuleiro):
    print("\n   0   1   2")

    for i in range(3):
        print(f"{i}  {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}")
        if i < 2:
            print("  ---+---+---")
    print()


def jogada_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False

    if tabuleiro[linha][coluna] != " ":
        return False

    return True


def verificar_vitoria(tabuleiro, jogador):
    
    for linha in tabuleiro:
        if linha[0] == jogador and linha[1] == jogador and linha[2] == jogador:
            return True

    
    for coluna in range(3):
        if (tabuleiro[0][coluna] == jogador and
            tabuleiro[1][coluna] == jogador and
            tabuleiro[2][coluna] == jogador):
            return True

    #  primeira diagonal vai validar a primeira diadonal usado um if para validar as combinações
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    # a segunda diagonal levou a mesma lógica
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


def trocar_jogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"


def main():
    tabuleiro = criar_tabuleiro()
    jogador = "X"

    print("===== JOGO DA VELHA =====")
    mostrar_tabuleiro(tabuleiro)

    while True:
        print(f"Jogador {jogador}")

        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida! Tente novamente.\n")
            continue

        tabuleiro[linha][coluna] = jogador

        mostrar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador):
            print(f"Parabéns! O jogador {jogador} venceu!")
            break

        if verificar_empate(tabuleiro):
            print("Deu velha!")
            break

        jogador = trocar_jogador(jogador)


main()
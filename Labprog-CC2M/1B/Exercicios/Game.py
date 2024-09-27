import random
import os


def jogo_da_velha():
    """
    Implementa um jogo da velha com o computador como adversário.
    """
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = 'X'
    jogadas = 0

    def imprime_tabuleiro():
        """
        Imprime o tabuleiro do jogo da velha.
        """
        print("-------------")
        for linha in tabuleiro:
            print("|", end="")
            for coluna in linha:
                print(f" {coluna} |", end="")
            print("\n-------------")

    def verifica_vitoria(jogador):
        """
        Verifica se o jogador atual venceu o jogo.
        """
        # Verifica linhas
        for linha in tabuleiro:
            if linha.count(jogador) == 3:
                return True

        # Verifica colunas
        for coluna in range(3):
            if tabuleiro[0][coluna] == jogador and tabuleiro[1][
                    coluna] == jogador and tabuleiro[2][coluna] == jogador:
                return True

        # Verifica diagonais
        if tabuleiro[0][0] == jogador and tabuleiro[1][
                1] == jogador and tabuleiro[2][2] == jogador:
            return True
        if tabuleiro[0][2] == jogador and tabuleiro[1][
                1] == jogador and tabuleiro[2][0] == jogador:
            return True

        return False

    def computador_jogada():
        """
        Faz a jogada do computador.
        """
        nonlocal jogador, jogadas
        while True:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                jogadas += 1
                jogador = 'O' if jogador == 'X' else 'X'
                break

    imprime_tabuleiro()
    while True:
        if jogadas == 9:
            print("Empate!")
            break
        if jogador == 'X':
            while True:
                try:
                    linha = int(
                        input(f"Jogador {jogador}, escolha a linha (0-2): "))
                    coluna = int(
                        input(f"Jogador {jogador}, escolha a coluna (0-2): "))
                    if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[
                            linha][coluna] == ' ':
                        tabuleiro[linha][coluna] = jogador
                        jogadas += 1
                        jogador = 'O' if jogador == 'X' else 'X'
                        break
                    else:
                        print("Posição inválida. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            imprime_tabuleiro()
        else:
            os.system('clear')
            print("Vez do computador...")
            computador_jogada()
            imprime_tabuleiro()
        if verifica_vitoria(jogador):
            print(f"Jogador {jogador} venceu!")
            break


jogo_da_velha()

import os
import time

game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_game():
  os.system('clear')
  print("\n\n")
  for i in range(len(game)):
    for j in range(len(game[i])):
      print(" " + game[i][j] + " ", end="")

      if j + 1 < len(game):
        print('|', end="")
    if i + 1 < len(game):
      print('\n-----------')
  print("\n\n")


def vez_do_jogador1():
  print_game()
  print("Vez do jogador 1:")
  linha = input("Linha: ")
  coluna = input("Coluna: ")
  try:
    if int(linha) > 2 or int(coluna) > 2:
      print("Posição inválida. Tente novamente.")
      time.sleep(2)
      vez_do_jogador1()
    if game[int(linha)][int(coluna)] == ' ':
      game[int(linha)][int(coluna)] = 'X'
    else:
      print("Posição já ocupada, tente novamente.")
      time.sleep(2)
      vez_do_jogador1()
    
  except Exception as e:
    print(e)
    time.sleep(2)
    vez_do_jogador1()


def vez_do_jogador2():
  print_game()
  print("Vez do jogador 2:")
  linha = input("Linha: ")
  coluna = input("Coluna: ")

  try:
    if int(linha) > 2 or int(coluna) > 2:
      print("Posição inválida. Tente novamente.")
      time.sleep(2)
      vez_do_jogador2()
    if game[int(linha)][int(coluna)] == ' ':
      game[int(linha)][int(coluna)] = 'O'
    else:
      print("Posição já ocupada, tente novamente.")
      time.sleep(2)
      vez_do_jogador2()
      
  except Exception as e:
    print(e)
    time.sleep(2)
    vez_do_jogador2()


def verifica_vitoria(jogador):
  for i in range(len(game)):
    if game[i][0] == game[i][1] == game[i][2] != ' ':
      print_game()
      print("Vitória do jogador " + jogador)
      return True

    if game[0][i] == game[1][i] == game[2][i] != ' ':
      print_game()
      print("Vitória do jogador " + jogador)
      return True

    if game[0][0] == game[1][1] == game[2][2] != ' ':
      print_game()
      print("Vitória do jogador " + jogador)
      return True

    if game[0][2] == game[1][1] == game[2][0] != ' ':
      print_game()
      print("Vitória do jogador " + jogador)
      return True
  return False


def verificaEmpate():
  ocupacao = 0
  for i in range(len(game)):
    for j in range(len(game[i])):
      if game[i][j] != ' ':
        ocupacao += 1
  if ocupacao == 9:
    print_game()
    print("Empate!")
    return True
  return False


vitoria = False
while not vitoria:
  vez_do_jogador1()
  if verifica_vitoria("1"):
    break

  if verificaEmpate() or vitoria:
    break

  vez_do_jogador2()
  if verifica_vitoria("2") or vitoria:
    break

  if verificaEmpate() or vitoria:
    break

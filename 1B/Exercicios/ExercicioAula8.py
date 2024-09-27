'''
  1 - Criar função que recebe uma matriz e um numero referente a diagonal e retorna 
  a multiplicação de todos os valores da diagonal escolhida
'''

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def multiplicarDiagonal(matriz, diagonal):
  TAMANHO = len(matriz)
  resultado = 1
  if diagonal < 0:
    for i in matriz:
      if diagonal < (TAMANHO * -1):
        diagonal *= -1
        diagonal -= 2
      resultado *= i[diagonal]
      diagonal -= 1
    return resultado
    
  diagonal -= 1
  for i in matriz:
    if diagonal >= TAMANHO:
      diagonal *= -1
    resultado *= i[diagonal]
    diagonal += 1
  return resultado


print(multiplicarDiagonal(matriz, 1))
'''
  2 - Criar uma função que calcule o determinante de uma matriz utilizando a função 1
  para o calculo das diagonais
'''

def calcularDeterminante(matriz):
  TAMANHO = len(matriz)
  resultado = 0
  for i in range(TAMANHO + 1):
    if i != 0:
      resultado += multiplicarDiagonal(matriz, i)
      resultado -= multiplicarDiagonal(matriz, i * -1)
  return resultado

print(calcularDeterminante(matriz))

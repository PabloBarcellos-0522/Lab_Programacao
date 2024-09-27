
  # 1. Inicialização de Matriz
def criar_matriz(linhas, colunas, valor):
  a = []
  for i in range(linhas):
    a.append([])
    for j in range(colunas):
      a[i].append(valor)
  return a
print(criar_matriz(3,4,0))


  # 2. Verificação de Matriz Identidade
def e_matriz_identidade(matriz):
  a = 0
  value = True
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      a += matriz[i][j]
  if a != len(matriz):
    value = False
  return value
print(e_matriz_identidade([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))


  # 3. Extração da Diagonal da Matriz
def extrair_diagonal(matriz):
  diagonal = []
  for i in range(len(matriz)):
    diagonal.append(matriz[i][i])
  return diagonal
print(extrair_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


  # 4. Cálculo do Traço da Matriz
def calcular_traco(matriz):
  traco = 0
  for i in range(len(matriz)):
    traco += matriz[i][i]
  return traco
print(calcular_traco([[1, 2], [3, 4]]))


  # 5. Verificação de Matriz Nula
def e_matriz_nula(matriz):
  for linha in matriz:
    for elemento in linha:
      if elemento != 0:
        return False
  return True
print(e_matriz_nula([[0, 0, 0], [0, 0, 0], [0, 0]]))


  # 6. Multiplicação de Matriz por Escalar
def multiplicar_escalar(matriz, escalar):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] *= escalar
  return matriz
print(multiplicar_escalar([[1, 2], [3, 4]], 3))


  # 7. Soma das Linhas e Colunas da Matriz
def somar_linhas(matriz):
  soma_linhas = [] 
  for i in range(len(matriz)):
    soma_linhas.append(sum(matriz[i]))
  return soma_linhas
print(somar_linhas([[1, 2, 3], [4, 5, 6]]))


def soma_colunas(matriz):
  soma_colunas = []
  for j in range(len(matriz[0])):
    soma_colunas.append(sum([matriz[i][j] for i in range(len(matriz))]))
  return soma_colunas
print(soma_colunas([[1, 2, 3], [4, 5, 6]]))


  # 8. Verificação de Matriz Esparsa
def e_matriz_esparsa(matriz):
  num_zeros = 0
  for linha in matriz:
    for elemento in linha:
      if elemento == 0:
        num_zeros += 1
  return num_zeros > (len(matriz) * len(matriz[0])) / 2
print(e_matriz_esparsa([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))

  
  # 9. Rotação de Matriz (90 Graus)
def rotacionar_matriz_90(matriz):
  n = len(matriz)
  rotacionada = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      rotacionada[j][n - i - 1] = matriz[i][j]
  return rotacionada
print(rotacionar_matriz_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


  # 10. Verificação de Simetria de Matriz
def e_matriz_simetrica(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(i + 1, n):
      if matriz[i][j] != matriz[j][i]:
        return False
  return True
print(e_matriz_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))
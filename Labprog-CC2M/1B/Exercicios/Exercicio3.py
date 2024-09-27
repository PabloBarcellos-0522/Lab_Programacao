'''
  1 - crie uma função matrix-addition(a,b)
    que recebe duas matrizes de mesma dimensão,
    caulcule e retorne a soma das duas matrizes.

  2 - crie uma função matrix-traspose(a,b)
    que retorne a matrix transposta de a.

  3 - crie uma função matrix-multiply(a,b)
    que retorne a multiplicação de a por b.
'''


def printMatrix(a):
  for i in range(len(a)):
    print(a[i])
  print("\n")


def matrixAddition(a, b):
  c = []

  for i in range(len(a)):
    c.append([])
    for j in range(len(a[i])):
      c[i].append(a[i][j] + b[i][j])
  return c


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printMatrix(matrixAddition(a, b))


def matrixTranspose(a):
  c = []

  for i in range(len(a[0])):
    c.append([])
    for j in range(len(a)):
      c[i].append(a[j][i])
  return c


d = [[1, 2], [3, 4], [5, 6]]
printMatrix(matrixTranspose(d))


def matrixMultiply(a, b):
  c = []

  for i in range(len(a)):
    c.append([])
    for j in range(len(b[0])):
      c[i].append(0)
      for k in range(len(b)):
        c[i][j] += a[i][k] * b[k][j]
  return c


e = [[1, 5], [3, 2]]
f = [[4, 8], [7, 0]]
printMatrix(matrixMultiply(e, f))





key1 = True
key2 = True
key3 = True

level = {
  "abrir porta" : [["voce abriu a porta", [255, 255, 255]], key1, key2, key3]
}
import time

def n_maiores(lista, n):
  maiores = []

  if n > len(lista):
    return lista
  
  for i in range(n):
    anterior = 0
    for number in lista:
      if number > anterior:
        anterior = number
    maiores.append(anterior)
    lista.remove(anterior)
  
  return maiores

start = time.time()

numeros = [5, 2, 3, 7, 8, 4, 1, 9]
print(n_maiores(numeros, 5))

end = time.time()

print(end - start)

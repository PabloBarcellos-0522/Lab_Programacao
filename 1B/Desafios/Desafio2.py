
def soma_n(lista, n):
  par = []
  metade = []
  lista = sorted(lista)

  for i in range(len(lista)):
    for j in range(len(lista)):
      if lista[i] + lista[j] == n and lista[i] != lista[j]:

        if par != [] and lista[i] == par[-1][-1] and lista[j] == par[-1][0]:
          for x in range(len(metade)):
            par.append(metade[x])
          return par
        
        par.append((lista[i], lista[j]))
        metade.insert(0, (lista[j], lista[i]))


numeros = [5, 2, 3, 7, 8, 4, 1, 9]
print(soma_n(numeros, 10))

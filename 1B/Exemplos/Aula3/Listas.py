'''
  lists: - Vários valores numa única variavel, indexada, ordenada, modificavel e permite duplicados.
'''

nomes = ['João', 'Maria', 'José', 'Ana']

print(type(nomes))
print(nomes)
print(nomes[0])

nomes.append('Carlos')
print(nomes)

nomes.pop(-1)
print(nomes)

print(f'Minha lista possui: {len(nomes)} pessoas')

lista = ['wagner', 39, True]
print(lista)

print(nomes[1:3])


if 'João' in nomes:
  print('João está na lista')
else:
  print('João não está na lista')

nomes.insert(1, 'pedrinho')
print(nomes)

v1 = [1, 2, 3]
v2 = [3, 4, 5]

v1.extend(v2)
print(v1)



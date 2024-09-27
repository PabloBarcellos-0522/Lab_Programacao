nomes = ['wagner', 'carlos', 'antonio', 'jose', 'wellington']

nomes_com_G = []

for i in range(len(nomes)):
  if nomes[i].find('g') != -1 or nomes[i].find('G') != -1:
    nomes_com_G.append(nomes[i])

print(nomes_com_G)


nomes_com_G = []
for nome in nomes:
  if 'g' in nome:
    nomes_com_G.append(nome)
print(nomes_com_G)
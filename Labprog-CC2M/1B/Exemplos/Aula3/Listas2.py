import time
import os

nomes = ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Pedro', 'Joana']

for nome in nomes:
  print(nome)

print('')

for i in range(len(nomes)):
  print(nomes[i])

os.system('clear')
a = 1
print(a)
while True:
  time.sleep(0.05)
  print(a*2)
  a *= 999
#--> Exercício 1
'''
1 - crie um programa que peça ao usuário para digitar seu nome e idade e informe se ele é maior de idade
'''

#--> Solução
print("informe seu nome:")
nome = input()

print("informe sua idade:")
idade = int(input())

if (idade >= 18):
  print("você é maior de idade, parabéns", nome + "!")
else:
  print("você é menor de idade, desculpe", nome, "!")
nome = "renato"

def imprimeNome():
  global nome
  global sobrenome

  nome = "Gabriel"
  sobrenome = "Henrique"
  print(f"Seu nome é: {nome}")

def imprimeSobrenome():
  print(f"Sobrenome: {sobrenome}")

imprimeNome()
imprimeSobrenome()
print(f"Seu nome é: {nome}")
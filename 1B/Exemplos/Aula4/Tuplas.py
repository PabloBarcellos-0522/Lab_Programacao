'''
Tuplas - É uma coleção ordenada, não-modificável e que permite duplicatas.
'''

frutas = ("pera", "banana", "morango", "banana", "laranja", "manga")

print(frutas)
print(type(frutas))

print(frutas[2])
print(frutas[2:4])

carros = ("cerato")
print(type(carros))

frutas = list(frutas)

print(frutas)
print(type(frutas))

frutas[2] = "tomate"
print(frutas)
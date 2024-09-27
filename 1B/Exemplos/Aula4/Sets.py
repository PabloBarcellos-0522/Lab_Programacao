'''
Sets - É uma coleção não ordenada, não-indexada e não-duplicada.
'''

frutas = {"pera", "banana", "morango", "Banana"}

print(frutas)
print(type(frutas))

coisas = {"wagner", "sandra", True, 1, 2}
print(coisas)



minhas_compras = {"carne", "cerveja", "carvao"}
compras_da_patroa = ["shampoo", "condicionador", "creme"]

minhas_compras.update(compras_da_patroa)
print(minhas_compras)


# CONJUNTOS
alunos_gp1 = {"andre", "carlos", "antonio", "jose", "joao"}
alunos_gp2 = {"clara", "andre", "joao", "pedro"}

# alunos_gp = alunos_gp1.union(alunos_gp2)
alunos_gp = alunos_gp1 | alunos_gp2
print(alunos_gp)

#alunos_2grupos = alunos_gp1.intersection(alunos_gp2)
alunos_2grupos = alunos_gp1 & alunos_gp2
print(alunos_2grupos)

# diferenca = alunos_gp1.difference(alunos_gp2)
# print(diferenca)
diferenca = alunos_gp1 - alunos_gp2
print(diferenca)

# diferenca = alunos_gp1.symmetric_difference(alunos_gp2)
# print(diferenca)
diferenca = alunos_gp1 ^ alunos_gp2
print(diferenca)
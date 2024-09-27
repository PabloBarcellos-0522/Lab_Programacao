def divisaoSegura(a, b):
  if b == 0:
    print("Erro, não dividir por zero")

  else:
    result = a/b
    print(result)
  

divisaoSegura(10, 0)
divisaoSegura(10, 3)


def calculoSalario(sBase, bonus, *desconto):
  # salario = sBase + (sBase * 0.1)
  print(sBase)
  print(bonus)
  print(desconto)

calculoSalario(1000, 500, 300, 200, 100)
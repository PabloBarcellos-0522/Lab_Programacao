import csv

clientes = [{
    'nome': 'João',
    'idade': 25,
    'salario': 5000.0,
    'sexo': 'F'
}, {
    'nome': 'Maria',
    'idade': 30,
    'salario': 6000.0,
    'sexo': 'F'
}, {
    'nome': 'Pedro',
    'idade': 35,
    'salario': 7000.0,
    'sexo': 'M'
}]

arquivo = 'clientes.csv'

with open(arquivo, mode='w') as file:
  witer = csv.DictWriter(file, fieldnames=['nome', 'idade', 'salario', 'sexo'])
  witer.writeheader()
  witer.writerows(clientes)

print(f'Arquivo {arquivo} criado com sucesso!')
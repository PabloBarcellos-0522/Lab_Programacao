import csv
import pandas as db

arquivo = 'clientes.csv'

with open(arquivo, 'r') as file:
  reader = csv.DictReader(file)
  clientes = list(reader)  # [linha for linha in reader]

for cliente in clientes:
  print(cliente)
  
df = db.DataFrame(clientes)
print(f"\n\n {df}")
import csv
import os

import pandas as db

arquivo = 'biblioteca.csv'

livros = []

try:
  with open(arquivo, 'r') as file:
    reader = csv.DictReader(file)
    livros = list(reader)
except Exception:
  with open(arquivo, mode='w') as file:
    witer = csv.DictWriter(file, fieldnames=['id', 'nome', 'genero', 'ano'])
    witer.writeheader()
    witer.writerows(livros)




def pegarUltimoId():
  ultimoId = 0
  for livro in livros:
    if int(livro['id']) > ultimoId:
      ultimoId = int(livro['id'])
      return ultimoId
  return 0




def pegarProximoID():
  ultimoId = 0
  for livro in livros:
    if int(livro['id']) > ultimoId:
      ultimoId = int(livro['id'])
  return ultimoId + 1




def cadastrarLivro():
  try:
    os.system('clear')
    print("Cadastrando novo livro: \n")
    nome = input("Nome: ")
    genero = input("Gênero: ")
    ano = int(input("Ano de lançamento: "))
    id = pegarProximoID()
  
    livros.append({'id': id, 'nome': nome, 'genero': genero, 'ano': ano})
  except Exception as e:
    print(e, "\n\n Erro, tente novamente")
    input("Aperte qualquer tecla...")
    cadastrarLivro()

  with open(arquivo, mode='w') as file:
    witer = csv.DictWriter(file, fieldnames=['id', 'nome', 'genero', 'ano'])
    witer.writeheader()
    witer.writerows(livros)




def listarLivros():
  os.system('clear')
  df = db.DataFrame(livros).sort_values(by=['id']).to_string(index=False)
  print("Lista de todos os livros cadastrados: ")
  print(f"\n {df}")
  
  if livros == []:
    os.system('clear')
    print("\n\nLista vazia")
    
  input("\n\nAperte enter para voltar...")




def buscarLivros():
  os.system('clear')
  print("Buscar pelo:\n")
  print("1 - Nome")
  print("2 - Gênero")
  print("3 - Ano de lançamento")
  print("4 - Voltar")

  try:
    opcao = int(input("\nOpção: "))
    resultados = []

    if opcao == 1:
      nome = input("Nome: ").lower()
      for livro in livros:
        if nome in livro['nome'].lower():
          resultados.append(livro)

    if opcao == 2:
      genero = input("Gênero: ").lower()
      for livro in livros:
        if genero in livro['genero'].lower():
          resultados.append(livro)

    if opcao == 3:
      ano = input("Ano de lançamento: ")
      for livro in livros:
        if ano in livro['ano']:
          resultados.append(livro)

    if opcao == 4:
      return

    
    if resultados == []:
      os.system('clear')
      print("\n\nNenhum livro encontrado")
    else:
      df = db.DataFrame(resultados).sort_values(by=['id']).to_string(index=False)
      print("\n\nlivros encontrados:")
      print(f"\n {df}")

    input("\n\nAperte enter para voltar...")
    
  except Exception as e:
    print(e, "\nErro, tente novamente")
    input("Aperte qualquer tecla...")
    buscarLivros()




def removerLivros():
  os.system('clear')
  df = db.DataFrame(livros).sort_values(by=['id']).to_string(index=False)
  print("Lista de todos os livros cadastrados: ")
  print(f"\n {df}")
  if livros == []:
    os.system('clear')
    print("\n\nLista vazia")
    input('\nEnter para voltar...')
    return

  print("\nQual o ID do livro que você deseja remover?")
  print("(Digite 0 para voltar)")
  id = input("\nID: ")
    
  excluido = 0
  if id.isnumeric():
    if int(id) == 0:
      return
      
    for livro in livros:
      if int(livro['id']) == int(id):
        livros.remove(livro)
        print("Livro removido com sucesso!")
        excluido += 1
  
    with open(arquivo, mode='w') as file:
      witer = csv.DictWriter(file, fieldnames=['id', 'nome', 'genero', 'ano'])
      witer.writeheader()
      witer.writerows(livros)
    input("\n\nAperte enter para voltar...")
  
  if excluido == 0:
    print("\n\nID Incorreto ou não existe")
    input("Tentar novamete...")
    removerLivros()
  



def menu():
  os.system('clear')
  print("\n1 - Cadastrar livro")
  print("2 - Listar livros")
  print("3 - Buscar livro")
  print("4 - Remover livro")
  print("5 - SAIR\n")
  
  try:
    return int(input("Digite a opção desejada: "))
  except Exception:
    return 0

while True:
  os.system('clear')
  escolha = menu()
  if escolha > 0 and escolha < 6:
    if escolha == 1:
      cadastrarLivro()
    elif escolha == 2:
      listarLivros()
    elif escolha == 3:
      buscarLivros()
    elif escolha == 4:
      removerLivros()
    elif escolha == 5:
      break
  else:
    input("\nOpção inválida...")

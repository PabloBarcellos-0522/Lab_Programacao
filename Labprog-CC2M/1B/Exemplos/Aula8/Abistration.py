# Abstração: abstrair detalhes e funcionalidades gerais e criar categorias (classes) que permitem detalhar conceitos.

from abc import ABC, abstractmethod

class Forma(ABC):
  @abstractmethod
  def area(self):
    pass

class Quadrado(Forma):
  def __init__(self, lado):
    self.lado = lado
  def area(self):
    return self.lado * self.lado

class Retangulo(Forma):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def area(self):
    return self.base * self.altura

class Triangulo(Forma):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def area(self):
    return (self.base * self.altura) / 2

figuras = [Quadrado(10),Triangulo(10, 20), Quadrado(20), Retangulo(10, 20), Quadrado(15), Retangulo(20, 30)]

print('O lado do primeiro quadrado é: ', figuras[0].lado)

figuras[1].base = -15

for f in figuras:
  print(f'A área da Figura é: {f.area()}')
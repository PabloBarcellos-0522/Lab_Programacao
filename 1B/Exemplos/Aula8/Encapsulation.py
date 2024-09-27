#encapsulation

class Conta:
  def __init__(self, saldo_inicial):
    self.__saldo = saldo_inicial

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor
    else:
      raise Exception('Operação Negada!')

  def depositar(self, valor):
    self.__saldo += valor

  def consultar_saldo(self):
    return self.__saldo

conta = Conta(100)
conta.sacar(101)
conta.depositar(200)

print(conta.consultar_saldo())
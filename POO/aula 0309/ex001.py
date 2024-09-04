# Exercício 1: Básico de Membros Públicos e Privados

# Crie uma classe ContaBancaria que tenha um atributo
# privado saldo e um atributo público titular. Inicialize ambos
# os atributos no método __init__. Em seguida, crie um método
# para depositar dinheiro e outro para exibir o saldo, garantindo
# que o saldo não possa ser acessado diretamente de fora da
# classe.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def saldo(self):
        print(self._ContaBancaria__saldo)

p1 = ContaBancaria('giovana', 0)
p1.depositar(100)
p1.saldo()

p2 = ContaBancaria('lavinia', 2)
p2.depositar(10000)
p2.saldo()

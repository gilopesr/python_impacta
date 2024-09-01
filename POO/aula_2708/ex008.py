# 8. Conta Bancária Simplificada
# Descrição: Crie uma classe ContaBancaria com atributos para o
# titular da conta, número da conta e saldo. Inclua métodos para
# depositar e sacar dinheiro, além de um método para exibir as
# informações da conta.


class ContaBancaria:
    def __init__(self, titular,numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self):
        valor = float(input("qual o valor que deseja depositar?: "))
        self.saldo += valor
        print(f'saldo atual R${self.saldo}')

    def sacar(self):
        saque = float(input('qual o valor que deseja sacar?: '))
        if saque > self.saldo:
            print('saldo insuficiente para saque')
        else: 
            self.saldo -= saque
            print('saque realizado com sucesso!')
            print(f'saldo atual é de R${self.saldo}')

    def info(self):
        print(f'TITULAR: {self.titular}')
        print(f'NUMERO DA CONTA: {self.numero_conta}')
        print(f'SALDO: {self.saldo}')

p1 = ContaBancaria('Giovana', 1234, 0)
p1.depositar()
p1.sacar()
p1.info()

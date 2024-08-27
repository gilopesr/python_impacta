# 2. Gerenciamento de Pessoas
# Descrição: Crie uma classe Pessoa com atributos para nome,
# idade e endereço. Inclua métodos para alterar o endereço e
# outro para exibir todas as informações da pessoa.

class Pessoa:
    def __init__(self,nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def MudarEndereco(self, endereco):
        self.endereco = endereco
    
    def info(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'Endereço: {self.endereco}')

p1 = Pessoa('Giovana', 19, 'Rua do Limão, 100')
print(p1.nome)
print(p1.idade)
print(p1.endereco)

p1.MudarEndereco('Rua abobrinha, 78')

p1.info()

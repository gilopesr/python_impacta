# Exercício 8: Agregação

# Crie uma classe Departamento e uma classe Funcionario.
# Um departamento pode ter vários funcionários, mas cada
# funcionário pode existir independentemente do departamento.
# A relação entre Departamento e Funcionario deve ser uma
# agregação.

# Defina a classe Funcionario com atributos nome e cargo.
# Defina a classe Departamento com um atributo para
# armazenar uma lista de Funcionarios.
# No exemplo de uso, crie um departamento e adicione alguns
# funcionários a ele.

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def adiciona_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo


funcionario1 = Funcionario('gabriela', 'diretora de arte')
dp = Departamento('marketing')
funcionario2 = Funcionario('julia', 'estilista')
dp2 = Departamento('estilista')

dp.adiciona_funcionario(funcionario1)
dp2.adiciona_funcionario(funcionario2)

print(f'Departamento: {dp2.nome}')
print(f'funcionarios:')
for funcionario in dp2.lista_funcionarios: 
    print(f'- {funcionario2.nome}')

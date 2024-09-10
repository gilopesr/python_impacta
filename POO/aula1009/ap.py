class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # def novaIdade(self, resp):
    #     if resp >= 18:
    #         print('idade aceita, patrão')
    #     else:
    #         print('digite uma idade valida')


    # def get_idade(self):
    #     return self.idade

    def set_idade (self, nova_idade):
        if nova_idade >= 18:
            print('idade aceita, patrão')
            self.idade = nova_idade
        else:
            print('digite uma idade valida')

baitola = Pessoa('Giovana', 19)

baitola.set_idade(15)


class Funcionario(Pessoa):
    def __init__(self, salario):
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_salario_anual(self, salario):
        calcSalario = salario * 12
        print(calcSalario)

class Departamento:
    def __init__(self, funcionario)
    self.funcionario = []

    def adiciona_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        




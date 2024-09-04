# Exercício 11 :


class Medico:
    def __init__(self, nome='', idade=0,especialidade=''):
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade
        self.lista_pacientes = []

    def adicionar_paciente(self,paciente):
        self.lista_pacientes.append(paciente)

    def exibir_pacientes(self):
        for paciente in self.lista_pacientes: 
            print(f'- Nome do Paciente: {paciente.nome}')
            print(f'- Idade: {paciente.idade}')
            print('-'*25          )

    def media_idade_pacientes(self):
        qntd = 0
        soma = 0
        for paciente in self.lista_pacientes: 
            soma += paciente.idade
            qntd += 1
        media = soma / qntd
        print(f'A media das idades é: {media:.2f}')

class Paciente:
    def __init__(self, nome='', idade=0):
        self.nome = nome 
        self.idade = idade

medico1 = Medico('flavia', 35, 'cirurgiã')
paciente1= Paciente('Giovana', 20)
paciente2=Paciente('lucas', 28)
paciente3=Paciente('bruna', 20)

medico1.adicionar_paciente(paciente1)
medico1.adicionar_paciente(paciente2)
medico1.adicionar_paciente(paciente3)


medico1.exibir_pacientes()
medico1.media_idade_pacientes()

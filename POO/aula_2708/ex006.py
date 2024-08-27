# 6. Controle de Animais de Estimação
# Descrição: Desenvolva uma classe AnimalDeEstimacao com
# atributos para nome, espécie e idade. Inclua métodos para
# alterar a idade do animal e outro para exibir as informações do
# animal.

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def MudarIdade(self, idade):
        self.idade = idade
    
    def info(self):
        print(f'Nome do Pet: {self.nome}')
        print(f'Espécie: {self.especie}')
        print(f'Idade: {self.idade}')

pet1 = AnimalDeEstimacao('nina', 'gato', 3)
pet1.MudarIdade(4)
pet1.info()


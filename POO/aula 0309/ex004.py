# Exercício 4: Validação em Setter

# Crie uma classe Pessoa com um atributo privado idade e um
# atributo público nome. Use um getter e um setter para idade, e
# adicione validação no setter para garantir que a idade não seja
# negativa. Se uma idade negativa for passada, defina a idade
# como 0 e imprima uma mensagem de aviso.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)

    def set_idade(self, idade):
        if idade <= 0:
            self.__idade = 0
            print("Idade invalida")
        else:
            self.__idade = idade
    
    def get_idade(self):
        return self.__idade
    
p1 = Pessoa('bruna', -5)
print(p1.get_idade())

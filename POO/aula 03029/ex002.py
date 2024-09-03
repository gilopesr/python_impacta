# Exercício 2: Getters e Setters Simples

# Crie uma classe Lampada com um atributo privado estado
# (ligado/desligado). Implemente métodos getters e setters para o
# atributo estado. O setter deve aceitar apenas os valores
# "ligado" ou "desligado" e alterar o estado da lâmpada de
# acordo.

class Lampada:
    def __init__(self, estado):
        self.set_estado(estado)

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, novo_estado):
        if novo_estado == 'ligado':
            self.__estado = novo_estado
        elif novo_estado == 'desligado':
            self.__estado = novo_estado

lampada = Lampada('ligado')
print(lampada.get_estado())
lampada.set_estado('desligado')
print(lampada.get_estado())
lampada.set_estado('ligado')
print(lampada.get_estado())
lampada.set_estado('desligado')
print(lampada.get_estado())
lampada.set_estado('ligado')
print(lampada.get_estado())
print('ops queimou')
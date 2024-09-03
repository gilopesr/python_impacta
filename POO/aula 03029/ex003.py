# Exercício 3: Uso de Property

# Modifique a classe Lampada do Exercício 2 para usar o
# decorator property. Reescreva os getters e setters usando a
# sintaxe de property. Certifique-se de que a funcionalidade de
# ligar e desligar a lâmpada permaneça a mesma.

class Lampada:
    def __init__(self):
        self.__estado = 'desligado'

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, novo_estado):
        if novo_estado == 'ligado':
            self.__estado = novo_estado
        elif novo_estado == 'desligado':
            self.__estado = novo_estado

    def ligar(self):
        self.estado = 'ligado'

    def desligar (self):
        self.estado = 'desligado'

lampada= Lampada()
print(lampada.estado)
lampada.ligar()
print(lampada.estado)
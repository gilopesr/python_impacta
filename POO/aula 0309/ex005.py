# Exercício 5: Property Avançada

# Crie uma classe Circulo com um atributo privado raio. Use a
# propriedade property para criar getters e setters para o raio.
# Além disso, adicione um método de propriedade area que
# calcule e retorne a área do círculo (área = π * raio^2). Garanta
# que o raio não possa ser negativo.

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, valor):
        if valor > 0:
            self.__raio = valor
        else:
            print('o valor deve ser maior que zero')

    @property
    def area(self):
        return 3.14 * (self.__raio**2)
    
circulo = Circulo(3)
print(circulo.area)

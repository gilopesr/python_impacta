# 4. Veículo
# Descrição: Implemente uma classe Carro com atributos para
# marca, modelo, ano e quilometragem. Inclua métodos para
# dirigir o carro, que aumenta a quilometragem, e outro método
# para exibir informações do carro.

class Veiculo:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def dirigir(self):
        print('vruuuuuuummm. . .')
        self.quilometragem += 1

    def info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Quilometragem: {self.quilometragem}km')

carro1 = Veiculo('honda', 'civic', 2019, 0)
carro1.dirigir()

class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia 
        
class Veiculo:    
    def __init__(self, ano, preco, motor ):
        self.ano = ano
        self.preco = preco
        self.motor = motor
        
    def exibir_detalhes(self):
        print(f'Ano: {self.ano} Preço: {self.preco} Motor: {self.motor}')

class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preço, motor)
        self.cor = cor 
        self.modelo = modelo
        
    def exibir_detalhes(self):
        print
    
        

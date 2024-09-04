# Exercício 10:

class Endereco:
    def __init__(self, rua='', numero=0,bairro='',complemento='',cep=''):
        self.rua= rua
        self.numero= numero
        self.bairro = bairro
        self.complemento= complemento
        self.cep= cep

    def exibir_dados(self):
        print(f'Rua: {self.rua}')
        print(f'Numero: {self.numero}')
        print(f'Bairro: {self.bairro}')
        print(f'Complemento: {self.complemento}')
        print(f'CEP: {self.cep}')


class Funcionario:
    def __init__(self, nome='', data_nasc='', sexo='', salario=0.0, endereco= Endereco()):
        self.nome= nome
        self.data_nasc= data_nasc
        self.sexo = sexo
        self.salario= salario
        self.endereco= endereco

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Data Nascimento: {self.data_nasc}')
        print(f'Sexo: {self.sexo}')
        print(f'Salario: {self.salario}')
        print('Endereço:')
        self.endereco.exibir_dados()
        
       

end = Endereco('rua do passaro', 100, 'sao lucas', 'casa', '128623-989')
func1= Funcionario('Giovana', '27/05/05', 'F', 10500.00, end)
func1.exibir_dados()
end.exibir_dados()

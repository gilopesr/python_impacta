class Pessoa:
    def __init__(self, nome, identificador):
        self.nome = nome 
        self.identificador = identificador

class PessoaJuridica(Pessoa):
    def __init__(self, nome, identificador, cnpj):
        super().__init__(nome, identificador)
        self.cnpj = cnpj
        
class PessoaFisica(Pessoa):
    def __init__(self, nome, identificador, rg, cpf):
        super().__init__(nome, identificador)
        self.rg = rg
        self.cpf = cpf
        
p1 = Pessoa("maria", 1)

p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")

print(p1.identificador)
print(p1.nome)

print(p_juridica.identificador) 
print(p_juridica.nome) 
print(p_juridica.cnpj) 
print(p_fisica.identificador) 
print(p_fisica.nome) 
print(p_fisica.rg) 
print(p_fisica.cpf)
class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome 
        self.cargo = cargo
        self.set_idade(idade)

    def set_idade(self,idade):
        while idade < 18:
            idade = int(input('idade invalida, insira nova idade: '))
        self.idade = idade
    
class membroEquipe(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade, cargo)
        self.__horas_trabalhadas = 0
        
    def get_horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    def adicionar_horas(self, horas):
        if horas > 0:
            self.__horas_trabalhadas += horas
        else:
            print('Hora deve ser maior que zero')
        
    def mostrar_detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
    
class Projeto:
    def __init__(self, nome_projeto):
        self.nome_projeto = nome_projeto
        self.membro = []
        
    def adicionar_membro(self, membro):
        self.membro.append(membro)
    
    def calcular_total_horas(self):
        total = 0
        for membro in self.membro:
            total += membro.get_horas_trabalhadas()
        return total
    
    def listar_membros(self):
        for membro in self.membro:
            membro.mostrar_detalhes()
            print(f'Horas trabalhadas: {membro.get_horas_trabalhadas()}')
    
    def remover_membro(self,nome):
        for membro in self.membro:
            if membro.nome == nome:
                self.membro.remove(membro)
                print('Membro removido')

#teste de uso

m1 = membroEquipe('emily', 25, 'Marketing')
m2 = membroEquipe('luiza', 38, 'diretora')
m3 = membroEquipe('felipe', 16, 'aprendiz')

projeto1 = Projeto('piloto')

projeto1.adicionar_membro(m1)
projeto1.adicionar_membro(m2)
projeto1.adicionar_membro(m3)

m1.adicionar_horas(10)
m2.adicionar_horas(20)
m3.adicionar_horas(5)

projeto1.listar_membros()

print(f'total de horas trabalhadas: {projeto1.calcular_total_horas()}')

projeto1.remover_membro('felipe')

projeto1.listar_membros()




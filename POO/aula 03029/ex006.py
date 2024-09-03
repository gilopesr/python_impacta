# Exercício 6: Associação Simples

# Crie uma classe Professor e uma classe Disciplina. Um
# professor pode estar associado a várias disciplinas, mas essa
# associação não implica em um relacionamento forte onde a
# existência da disciplina depende do professor. A relação deve
# ser uma associação simples.

# • Defina a classe Disciplina com um atributo nome.
# • Defina a classe Professor com um atributo nome e uma
# lista de Disciplinas.
# • No exemplo de uso, crie algumas disciplinas e associe-as a um
# professor.

class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Professor:
    def __init__(self, nome):
        self.nome = nome 
        self.disciplinas = []
    
    def adiciona_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


professor1 = Professor('ricardo')
matematica = Disciplina('matematica')
historia = Disciplina('historia')
geografia = Disciplina('geografia')

professor1.adiciona_disciplina(matematica)
professor1.adiciona_disciplina(geografia)

print(f'professor: {professor1.nome}')
print(f'materias:')
for disciplina in professor1.disciplinas:
    print(f'- {disciplina.nome}')

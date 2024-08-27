# 5. Registro de Alunos
# Descrição: Crie uma classe Aluno com atributos para nome,
# matrícula e curso. Adicione métodos para mudar o curso do
# aluno e outro para exibir as informações do aluno.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def MudarCurso(self, curso):
        self.curso = curso
        print('Curso mudado com sucesso!')

    def info(self):
        print(f'Nome Aluno(a): {self.nome}')
        print(f'Matricula: {self.matricula}')
        print(f'Curso: {self.curso}')

aluno1 = Aluno('Giovana', 2401570, 'ADS')
aluno1.info()
aluno1.MudarCurso('BD')
aluno1.info()
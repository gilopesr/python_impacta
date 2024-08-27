# 3. Sistema de Biblioteca
# Descrição: Desenvolva uma classe Livro com atributos para título,
# autor, ano de publicação e disponibilidade. Adicione métodos
# para emprestar e devolver o livro, alterando seu status de
# disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade
        
    def Emprestar(self):
        if self.disponibilidade == 'disponivel':
            print('Emprestimo concluido! não se esqueça de devolver!')
            self.disponibilidade = 'emprestado'
        else:
            print('O livro não está disponivel no momento')

    def Devolver(self):
        self.disponibilidade = 'disponivel'
        print('Obrigada pela Devolução')


livro1= Livro('harry potter', 'JK', 2010, 'disponivel')

print(livro1.disponibilidade)
livro1.Emprestar()
print(livro1.disponibilidade)
livro1.Emprestar()
livro1.Devolver()
print(livro1.disponibilidade)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import datetime

# Criação do engine e da sessão
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Definição da classe Autor
class Autor(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)

    def __repr__(self):
        return f'<Autor(nome={self.nome}, livros={self.livros})>'

# Definição da classe Livro
class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = relationship('Autor', backref='livros')

    def __repr__(self):
        return f'<Livro(titulo={self.titulo}, autor={self.autor.nome})>'

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

def adicionar_autor(nome):
    autor = session.query(Autor).filter_by(nome=nome).first()
    if not autor:
        autor = Autor(nome=nome)
        session.add(autor)
        session.commit()

def adicionar_livro(titulo, autor_nome):
    autor = session.query(Autor).filter_by(nome=autor_nome).first()
    if not autor:
        print(f'Autor "{autor_nome}" não encontrado.')
        return

    livro = Livro(titulo=titulo, autor=autor)
    session.add(livro)
    session.commit()

def consultar_livros():
    livros = session.query(Livro).all()
    for livro in livros:
        print(livro)

def consultar_autor():
    autores = session.query(Autor).all()
    for autor in autores:
        print(autor.nome)
        for livro in autor.livros:
            print(f'- {livro.titulo}')

def main():
    while True:
        print('\nEscolha uma opção:')
        print('1. Adicionar Autor')
        print('2. Adicionar Livro')
        print('3. Consultar Livros')
        print('4. Consultar Autores')
        print('5. Sair')

        opcao = input('Opção: ')
        if opcao == '1':
            nome = input('Nome do Autor: ')
            adicionar_autor(nome)
        elif opcao == '2':
            titulo = input('Título do Livro: ')
            autor_nome = input('Nome do Autor: ')
            adicionar_livro(titulo, autor_nome)
        elif opcao == '3':
            consultar_livros()
        elif opcao == '4':
            consultar_autor()
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
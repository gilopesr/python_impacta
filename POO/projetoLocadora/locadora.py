from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import datetime


#criação e conexão do banco de dados com POO
engine = create_engine('sqlite:///locadora.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Diretor(Base):
    __tablename__ = 'diretores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sexo = Column(String)
    nacionalidade = Column(String)

class Filme(Base):
    __tablename__ = 'filmes'
     
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    anoLancamento = Column(Integer)
    qtdDisponivel = Column(Integer)
    diretor_id = Column(Integer, ForeignKey('diretores.id'))
    diretor = relationship('Diretor', backref='filmes')
    
class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    
    data = 0
    disponibilidade = 0
    
    
class Cliente(Base):
    __tablename__ = 'clientes'
    
    nome = Column(String)
    dataNasc = Column(String)
    sexo = Column(String)
    cpf = Column(String)
    
    
    
# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)
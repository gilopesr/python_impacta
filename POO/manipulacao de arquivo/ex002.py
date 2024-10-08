##Exercício 2: Manipulação de Arquivos CSV
##Escreva um programa que crie um arquivo CSV chamado alunos.csv, com as colunas "Nome" e "Idade".
##O programa deve inserir os dados de três alunos e, em seguida, ler o arquivo e exibir os dados no console.

import csv

colunas = ['nome', 'idade']

alunos = [
    ['Bruna', 18],
    ['Giovana', 19],
    ['Lavinia', 18],
]

with open('alunos.csv', 'w', newline='',
    encoding='utf-8') as arquivo_csv:

    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(alunos)

with open('alunos.csv', 'r', newline='',
    encoding='utf-8') as arquivo_csv:

    leitor = csv.reader(arquivo_csv, delimiter=';')
    novo_aluno = list(leitor)
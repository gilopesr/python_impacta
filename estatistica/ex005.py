# Exercicio 5
# Faça um Programa que peça as o nome e as três notas de 5 alunos, calcule e armazene
# em uma lista a média de cada aluno, imprima as médias e diga quais alunos foram
# aprovados e quais foram reprovados usando como parâmetro a média 6,0.

import numpy as np

for i in range (5):
  aluno= input(f'insira o nome do {i+1} aluno: ')
  n1= float(input('digite a 1° nota: '))
  n2= float(input('digite a 2° nota: '))
  n3= float(input('digite a 3° nota: '))
  lista=[n1, n2, n3]
  media = np.median(lista)
  if media >= 6:
    print(f'O aluno {aluno} foi aprovado com a média {media:.1f}')
  else:
    print(f'O aluno {aluno} foi reprovado com a média {media:.1f}')

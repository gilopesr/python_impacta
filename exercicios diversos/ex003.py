#3) Os valores dos ingressos de um cinema é cobrado
#  de acordo com a idade da pessoa.
#  veja a tabela abaixo
#  idade        valor (R$)
#   x <= 3         0
#   3 < x <= 12    20
#   x > 12        25
#Faça um programa que peça a quantidade de pessoas que entraram no cinema e
#A idade delas e informe a arrecadação da bilheteria

idades = []

qnt = int(input('Quantidade de pessoas:'))

for pessoa in range(qnt):
  idade = int(input(f'{pessoa+1}° Pessoa - Idade: '))
  idades.append(idade)

arrecadado = 0

for idade in idades:
  if idade <= 3:
    pass
  elif idade > 3 and idade <= 12:
    arrecadado += 20
  elif idade > 12:
    arrecadado += 25

print(f'O valor arrecadado foi de R${arrecadado:.2f}')

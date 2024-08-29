#07) Faça um programa que peça um número inteiro e determine se ele é ou não um
#número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.
  
num = int(input("Digite um número: "))
cont = 0

for i in range (1, num + 1):
  if num % i == 0:
    cont += 1
if cont == 2:
  print (f"O numero {num} é primo")
else:
  print(f"O numero {num} não é primo")

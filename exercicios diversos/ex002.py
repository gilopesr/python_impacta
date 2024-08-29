# 2) Dado um número N escreva um programa que determine a soma
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
# OBS: N deve ser um número inteiro e positivo e N > 1

n = int(input('Qual o valor de N '))
s = 1

if n != int and n < 1:
  print('N deve ser inteiro')

else:
  for i in range(2,n+1):
    s = s + 1/i

print (s)

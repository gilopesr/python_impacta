# Exercicio 6
# Faça um Programa que leia uma lista de 5 números inteiros, mostre a soma e a
# multiplicação dos números.

lista= [10,15,20,25,30]
soma= 0
mult= 1
for i in range (5):
  mult= mult * lista[i]
  soma= soma + lista[i]
print(f'soma igual= {soma}')
print(f'multiplicação= {mult}')

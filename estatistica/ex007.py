# Exercicio 7
# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
# o quadrados dos elementos do vetor.

quadrado =[]
A = [1,2,3,4,5,6,7,8,9,10]
for i in range (len(A)):
  x =A[i] ** 2
  quadrado.append(x)
print(quadrado)

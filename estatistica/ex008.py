# Exercicio 8
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.
A = []
B = [1,3,5,7,9,11,13,15,17,19]
C = [2,4,6,8,10,12,14,16,18,20]
for i in range (10):
  A.append(B[i])
  A.append(C[i])
print(A)

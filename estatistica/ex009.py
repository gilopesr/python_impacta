# Exercicio 9
# Faça uma lista com 20 números de 1 a 20 e simule um sorteio de 5 números
# De o print dos 5 números
import random
S = []
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range (5):
  x= random.choice(A)
  S.append(x)
  A.remove(x)
  S.sort()
print(A)
print(S)

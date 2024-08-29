#exercicio 10
# faça uma lista com 10 números aleatorios e depois imprima

import random
lista = []
for c in range(10):
  x = random.randint(1, 100)
  lista.append(x)
for c in lista:
  print(c, end=" ")

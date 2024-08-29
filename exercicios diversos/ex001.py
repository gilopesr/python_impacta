# 1) Faça um programa que calcule o quadrado dos
# números pares de uma lista indo de 1 até 99
# guardar esses valores em uma nova lista

lista = []
lista2 = []
for i in range(2,100,2):
  quadrado = i ** 2
  lista.append(quadrado)
  lista2.append(i)
print(lista2)
print(lista)

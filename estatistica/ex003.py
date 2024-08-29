# resolva usando uma lista
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

import numpy as np
import statistics as sta

lista =[]
for i in range(4):
  nota = float(input("Insira a nota "))
  lista.append(nota)
media = np.median(lista)
print(f"Notas = {lista}")
print(f"Média = {media:.1f}")

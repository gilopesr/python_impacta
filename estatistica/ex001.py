# usando uma lista no Python
# Funções estatísticas no Python
# média, mediana, moda, variância, DP

import numpy as np
import statistics as sta
lista = [31,18,18,18,18,15,48,17,19,34,62,17,21,22]
media = np.median(lista)
moda = sta.mode(lista)
mediana = np.mean(lista)
variancia = np.var(lista)
DP1 = np.std(lista)
DP2 = np.sqrt(variancia)
print(f"media = {media}")
print(f"moda = {moda}")
print(f"mediana = {mediana}")
print(f"variância = {variancia}")
print(f"DP = {DP1}")
print(f"DP = {DP2}")

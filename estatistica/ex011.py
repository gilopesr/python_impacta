#exercico 11
#Faça mu programa que receba a temperatura media
#de cada mes do ano e armazene-as em uma lista.
#Em seguida, calcule a media e o desvio pardrao das temperaturas
#imprima o desvio padrao
# Determine um intervalo [media - DP , media + DP]
# conte quantas temperaturas estão acima, abaixo e dentro do interval
import numpy as np
import statistics as sta

lista = []
acima = []
abaixo = []
for i in range (12):
 temp = float(input(f"insira a temperatura media do {i+1}mês"))
 lista.append(temp)
 media = np.median(lista)
 DP = np.std(lista)
 print(f"media = {media}")
 print(f"DP = {DP}")
 menos= media - DP
 mais= media + DP
for i in range(12):
  if temp >= mais







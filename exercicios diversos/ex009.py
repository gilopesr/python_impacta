# 09) Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
# em seus saltos e depois informe a média dos saltos conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular a média).
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da
# execução, portanto não são ordenados.

# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

import statistics as std
lista = []
saltos = []
nome = input("insira o nome do atleta: ")
for i in range(5):
  salto = float( input (f'insira o {i+1}° salto: '))
  lista.append(salto)
  saltos.append(salto)

maior = max(lista)
menor = min(lista)

lista.remove(max(lista))
lista.remove(min(lista))

media = std.mean(lista)

print(f'Atleta: {nome}')

print(f'Primeiro salto: {saltos[0]}m \nSegundo salto: {saltos[1]}m \nTerceiro salto: {saltos[2]}')
print(f'Quarto salto: {saltos[3]}m \nQuinto salto: {saltos[4]}m')

print(f'Melhor Salto: {maior}m \nPior salto:  {menor}m')
print(f'Media dos demais saltos: {media}m')

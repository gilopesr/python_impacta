# 8) Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco saltos.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
# e depois informe o nome, os saltos e a média dos saltos.

import statistics as st

saltos=[]
nome= input('Digite o seu nome:')
for i in range(5):
  salto= float(input(f'Digite o valor {i+1}° do salto: '))
  saltos.append(salto)
media= st.mean(saltos)
print(f'O atleta {nome}, obteve os saltos {saltos} com a media de {media:.1f}')

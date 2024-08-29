#11) Faça uma lista com idades e outra com a alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem
#altura inferior à média de altura desses alunos.

import statistics as std

idades = [13,12,14,15,14,13,14,15,12,13,13,13,13,14,15,12,15,14,15,13,15,14,12,13,15,14,15,13,14,15]
altura = [151,165,145,154,153,160,155,139,140,160,150,155,152,159,163,156,147,158,148,160,159,152,154,157,149,145,157,160,145,160]
cont = 0
media= std.mean(altura)

for i in range(30):
  if idades[i] > 13:
    if altura[i] < media:
      cont +=1
print(cont)
print( media)

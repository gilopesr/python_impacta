# 14) Dada a lista [8,10,5,-3,5,7,1,9] ordenar a lista sem usar o comando sort
# nome:

lista=[8,10,5,-3,5,7,1,9]
ordem = []
i = 0
maior = lista[0]
while i < 8:
  if lista[i] < maior:
    ordem.append(lista[i])
    i+=1
  else:
    menor = lista[i]
print(ordem)

# 04) faça uma função que dado uma lista ele dobre
# todos os números da lista e imprima as duas listas

def dobralista (lista):
  i = 0
  while i < len (lista):
    lista[i] *=2
    # lista [i] = lista [i] * 2
    i += 1

valores = [5,85,3,81,8,54,7,-9]
dobralista(valores)

print(f'lista de valores dobrados: {valores}')

#4) Dada a lista L = [2,5,4,-3,8,-3,2,5,4,5,12,-78,12,68,-25,74]
#Determine:
#O maior número
#O menor número
#Uma lista com os números positivos
#Uma lista com os números negativos

L = [2,5,4,-3,8,-3,2,5,4,5,12,-78,12,68,-25,74]
listaNegativos = []
listaPositivos = []

min = min(L)
max = max(L)

for i in L:
  if i < 0:
    listaNegativos.append(i)
  else:
    listaPositivos.append(i)

print(f"Minimo: {min}")
print(f"Maximo: {max}")
print(f"Positivos: {listaPositivos}")
print(f"Negativos: {listaNegativos}")

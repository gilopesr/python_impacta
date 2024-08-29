# 19) Desenvolva um programa que apresente a soma dos valores pares
# e dos valores ímpares da lista [21, 5, 34, 8, 16, 7, 3, 24, 36, 21, 75, 12]

lista = [21, 5, 34, 8, 16, 7, 3, 24, 36, 21, 75, 12]
i = 0
par = 0
impar = 0
while i < 12:
  if lista[i] % 2 == 0:
    par = par + lista[i]
    i += 1
  else:
    impar = impar + lista[i]
    i+=1
print(f'soma dos numeros pares = {par}\n soma dos numeros impares = {impar}')

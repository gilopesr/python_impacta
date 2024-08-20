#Exercício 1: Números Primos
#Crie um programa que encontre e imprima os 20 primeiros números primos.
# Um número é considerado primo se ele é maior que 1 e possui exatamente
# dois divisores: 1 e ele mesmo. Utilize um loop while para iterar até
# encontrar 20 números primos e um loop for para contar a quantidade de
# divisores de cada número.

primos = []
num = 2
while len(primos) < 20:
    cont = 0
    for i in range (1, num + 1):
        if num % i == 0:
            cont += 1
    if cont == 2:
      primos.append(num)
    num += 1
print(primos)
# 15) Números de Armstrong
# Um número de Armstrong é um número de N dígitos onde a soma de cada dígito,
# elevado a N, é igual ao próprio número.
# Veja um exemplo com um número de 3 dígitos em base 10:
# 153 = 1³ + 5³ + 3³ =  1 + 125 + 27 = 153
# Escreva um programa peça para o usuário digitar um número e calcule o número
# de Armstrong.

num = input('digite um número para calcular o numero de Armstrong: ')
qntd = len(num)
armstrong = 0
while int(num) > 0:
  armstrong += (int(num) % 10)**qntd
  num = (int(num)/10)
print(armstrong)

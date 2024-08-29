# pergunte o tamanho da amostra
# calcule a Média e o Desvio Padrão da amostra

lista =[]
n = int(input("Qual o tamanho da amostra? "))
for i in range(n):
  numero = float(input("informe o número "))
  lista.append(numero)
media = np.median(lista)
DP = np.std(lista)
print(f"media = {media}")
print(f"DP = {DP:.2f}")

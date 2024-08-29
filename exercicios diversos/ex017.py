# Ex 17) faça um código que pergunte o valor do financiamento, números de parcela
#        taxa de juros e determine o valor do financiamento
#        para isso você vai usar a formula abaixo
# P é a parcela,
# PV = valor do financiamento ou empréstimo
# i = taxa de juros
# n = número de parcelar.

pv = float(input("Qual o valor do financiamento? "))
i = float(input("Qual a taxa de juros mensal? "))
n = float(input("Em quantos meses será realizado o financiamento? "))
p = pv * ((1 + i / 100) ** n * i / 100) / ((1 + i / 100) ** n -1)
print(f"O valor da parcela será de R${p:.2f}")

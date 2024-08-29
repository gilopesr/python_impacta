#5) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
#Cada número a partir do 3° é calculado pela soma dos dois números anteriores
#Peça para o usuário digitar quantidade de termos da sequência e imprima a sequência
#de Fibonacci até o n−ésimo termo.

qntd = int(input('insira a quantidade da sequencia: '))
numero = 1
anterior = 0
for i in range (qntd):
    print(numero,end=' ')
    aux = numero
    numero += anterior
    anterior = aux

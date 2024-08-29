#5) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
#Cada número a partir do 3° é calculado pela soma dos dois números anteriores
#Peça para o usuário digitar quantidade de termos da sequência e imprima a sequência
#de Fibonacci até o n−ésimo termo.

n = int(input('Digite até onde a sequencia de Fibonacci deve ir: '))

fib = [1, 1]

for i in range(2, n):
  fib.append(fib[i - 1] + fib[i - 2])

print(f'A sequencia da Fibonacci até o {n}° termo\n{fib}')

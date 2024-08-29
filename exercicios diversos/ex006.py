#9) Em analise combinatória usamos uma formula para o aranjo
#e outra formula para a combinação
#n! = n * (n-1) * (n-2) * ... * 2 * 1 para n >= 2 e n = int
#A = n! / (n-p)!
#C = n! / (p! * (n-p)!)
#Faça uma pesquisa na internet sobre esse assunto
#determine A e C para n=10 e p=7

import math
n = int(input('Digite o numero n: '))
p = int(input('Digite o numero p: '))

A = math.factorial(n)/math.factorial(n-p)
C = math.factorial(n)/ (math.factorial(p) * math.factorial(n-p))
""
print(f"A{n},{p} = {A}")
print(f"C{n},{p} = {C}")

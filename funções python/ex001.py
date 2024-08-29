# 01)

def par (n):
  if n % 2 == 0:
    return (f'sim, o número {n1} é par')
  else:
    return (f'não, o número {n1} é impar')

n1 = int(input('digite um numero para saber se é par ou impar: '))
resp = par(n1)
print(f'{n1} é par? {resp}')

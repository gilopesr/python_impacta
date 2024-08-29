# faça um programa que tenha uma função chamada área(), que
#recebe as dimensões de um terreno retagular e mostre sua área:

def area(larg,comp):
  A= larg * comp
  print(f'a área do terreno {larg}x{comp} é de {A} m²')

print('⋅˚₊‧ ୨୧ ‧₊˚ ⋅'*3)
print('       Área do terreno')
print('⋅˚₊‧ ୨୧ ‧₊˚ ⋅'*3)
l = float(input('Qual é a largura em metros?: '))
c = float(input('Qual é o comprimento em metros?: '))
area(l,c)

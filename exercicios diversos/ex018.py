# 18) faça um código que leia três números e mostre o maior
n1 = float(input("1° número "))
n2 = float(input("2° número "))
n3 = float(input("3° número "))
if n1>n2 and n1>n3:
   print(n1," é o maior número")
elif n2>n1 and n2>n3:
   print(n2," é o maior número")
else:
  print(n3," é o maior número")

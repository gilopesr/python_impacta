# Faça um programa que lê uma nota e atribua o
# seguinte conceito
# Entre 9 e 10 = A
# Entre 8 e 7 = B
# Entre 6 e 5 = C
# Entre 4 e 3 = D
# Entre 2 , 1 e 0 = E

nota = float(input("Qual sua nota? "))
if nota >= 9:
  print(f"conceito = A")
elif nota >= 7:
  print(f"conceito = B")
elif nota >= 5:
  print(f"conceito = C")
elif nota >= 3:
  print(f"conceito = D")
else:
  print(f"conceito = E")

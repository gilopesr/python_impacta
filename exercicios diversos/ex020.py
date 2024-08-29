# faça um codigo que calcule a média de
# três notas
# media >= 6 escreva aprovado
# media < 6 escreva reprovado

n1 = float(input("Digite o 1° número "))
n2 = float(input("Digite o 2° número "))
n3 = float(input("Digite o 3° número "))
media = (n1 + n2 + n3) / 3

if media >= 6:
  print("o aluno foi aprovado com media", media)
else:
  print(f"o aluno foi reprovado com média {media}")

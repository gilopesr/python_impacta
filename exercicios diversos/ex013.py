# 13) O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 8,90
# Bauru Simples   101     R$ 13,30
# Bauru com ovo   102     R$ 15,00
# Hambúrguer      103     R$ 12,50
# Cheeseburguer   104     R$ 13,00
# Refrigerante    105     R$ 6,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
# geral do pedido.
# Imprima a conta contendo os produtos, valores unitários e valores total
# Entre com a valor do dinheiro dado pelo cliente
# calcule e imprima na tela o troco

produtos = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburger', 'Refrigeramte']
codigos = [100, 101, 102, 103, 104, 105]
precos = [8.90, 13.30, 15, 12.50, 13, 6]
print("=" * 34)
print('            CARDAPIO')
print("=" * 34)
print("Especificação     Código    Preço")
print("Cachorro Quente    100     R$ 8,90")
print("Bauru Simples      101     R$ 13,300")
print("Bauru com ovo      102     R$ 15,00")
print("Hambúrguer         103     R$ 12,50")
print("Cheeseburguer      104     R$ 13,00")
print("Refrigerante       105     R$ 6,00")

cod100 = 0
cod101 = 0
cod102 = 0
cod103 = 0
cod104 = 0
cod105 = 0
total = [cod100, cod101, cod102, cod103, cod104, cod105]
for i in range(6):
  cod = int(input('Digite o código do produto: '))
  quant = int(input('Digite a quantidade: '))
  continuar = int(input("Digite 1 para continuar ou 2 para finalizar seu pedido: "))
  if cod == 100:
    total [0] = precos[0] * quant
  elif cod == 101:
    total [1] = precos[1] * quant
  elif cod == 102:
    total [2] = precos[2] * quant
  elif cod == 103:
    total [3] = precos[3] * quant
  elif cod == 104:
    total [4] = precos[4] * quant
  else:
    total [5] = precos[5] * quant
  if continuar == 2:
    break
valorTotal = sum(total)

for i in range(len(total)):
  if total[i] != 0 :
    print(f"Produto: {produtos[i]}   valor Unitário: R${precos[i]:.2f} reais    Valor total: {total[i]:.2f}")

print(f"Total: R${valorTotal:.2f}")
dinheiro = float(input('Digite o valor entregue '))
if dinheiro != total:
  troco = dinheiro- valorTotal
  print(f'seu troco é de R${troco}')
else:
  print('pagamento concluido sem troco!')

# Preencha um dicionário com as informações de 5 produtos
# - Utilize o nome do produto como chave e o preço como valor.
# - Solicite os dados ao usuário
# - Percorra o dicionário e exiba o nome dos produtos com preço
# superior a R$ 50,00.
# Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {&#39;caneta&#39;: 3.0, &#39;Pen drive&#39;: 100.0,&#39;Teclado&#39;: 30.0, &#39;Lápis&#39;: 1.5}

produtos = {}
while len(produtos) < 5:
    chave1 = input(f'insira o nome do produto: ')
    valor = int(input('insira o preço: '))
    produtos[chave1] = valor

for chave, valor in produtos.items():
    if valor > 50:
        print(f'produto: {chave} --> preço: {valor}')
    
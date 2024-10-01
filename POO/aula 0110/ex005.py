# Exercício 5: Sistema de Pagamento com Verificação
# Implemente uma função `processar_pagamento(valor)` que recebe o valor de uma compra.
# Se o valor for negativo ou zero, lance uma exceção personalizada `ValorInvalidoError`. Use
# `try-except` para tratar o erro e solicite ao usuário que insira um valor válido até que o
# processo seja concluído com sucesso.

class ValorInvalidoError(Exception):
    pass

def processar_pagamento(valor):
    while True:
        try:
            if valor <= 0:
                raise ValorInvalidoError('ERRO: o valor é invalido')
            return valor
        except ValorInvalidoError as i:
            print(i)
            valor = float(input('insira o valor da compra: '))
            

valor = float(input('insira o valor da compra: '))
compra = processar_pagamento(valor)
print(compra)
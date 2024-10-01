# Exercício 2: Função de Raiz Quadrada com Tratamento de Exceções
# Crie uma função `calcular_raiz_quadrada(numero)` que recebe um número como argumento
# e retorna a raiz quadrada desse número. Se o número for negativo, a função deve lançar
# uma exceção personalizada `NumeroNegativoError` e capturar essa exceção para exibir
# uma mensagem de erro. Dica: Você pode usar o módulo math para calcular a raiz quadrada
# usando o método `math.sqrt(numero) `

import math

class NumeroNegativoError(Exception):
    pass

def calcular_raiz_quadrada():
    try:
        numero = int(input('digite um numero: '))
        if numero < 0:
            raise NumeroNegativoError('ERRO: O número deve ser positivo!')
        else:
            return math.sqrt(numero)
    except NumeroNegativoError as e:
        print(e)

raiz = calcular_raiz_quadrada()
print(f"Raiz quadrada: {raiz}")

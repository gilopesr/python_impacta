# Exercício 1: Funções como argumentos para outras funções
# Implemente uma função chamada `executar_operacao` que receba uma função de operação matemática 
# e dois números.
# A função deve executar a operação matemática nos dois números fornecidos.
# Implemente a chamada à função passada e retorne o resultado

##Teste a função 'executar_operacao' passando as funções 'somar' e 'subtrair'

##Desafio: Adicione mais operações, como multiplicação e divisão.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


def executar_operacao(funcao, x, y):
    print(funcao(x,y))
    
executar_operacao(somar, 5, 5)
executar_operacao(subtrair, 10, 5)
executar_operacao(mult, 48, 90)
executar_operacao(div, 786, 6)

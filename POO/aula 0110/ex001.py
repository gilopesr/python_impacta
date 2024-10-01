# Exercício 1: Validação de Entrada Numérica
# Crie uma função `ler_numero( )` que solicita ao usuário que insira um número inteiro. Se o
# usuário inserir algo que não seja um número inteiro, a função deve levantar uma exceção
# personalizada `EntradaInvalidaError` e tratar a exceção para exibir uma mensagem
# amigável. Dica: Para verificar se uma string é composta por dígitos numéricos, utilize o
# método `isdigit( )`, que retorna True se a string é composta por números.
 
class EntradaInvalidaError(Exception):
    pass
 
def ler_numero():
    numero = input('digite um numero: ')
    
    if numero.isdigit():
        return int(numero)
    else:
        raise EntradaInvalidaError('filho da puta coloca o numero certo !!!!!!!')
        
try:
    numero = ler_numero()
    print(f"Número inserido: {numero}")
except EntradaInvalidaError as e:
    print(e)
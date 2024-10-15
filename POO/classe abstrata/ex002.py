## Exercício 2: Funções como valor de retorno de outras funções
## Implemente uma função chamada `criar_multiplicador` que receba um número `n` e retorne uma função
# que multiplica o argumento de entrada por `n`.

# def criar_multiplicador(n):
#     def multiplicante(x):
#         return n * x
#     return multiplicante
           
# triplo = criar_multiplicador(3)
# print(triplo(5))
    


## Desafio: Crie uma função `criar_calculadora` que retorne diferentes operações matemáticas 
# baseadas em um parâmetro.

def criar_calculadora(n):
    def multiplicacao(x):
        return n * x
    
    def soma(d):
        return n + d
    
    return soma, multiplicacao

cinco = criar_calculadora(5)
print(cinco(10))
    

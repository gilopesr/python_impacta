# Exercício 4: Cálculo de Média com Validação
# Escreva uma função `calcular_media(notas)` que recebe uma lista de notas e calcula a
# média. Se a lista contiver um valor que não seja um número (exemplo: uma string), a função
# deve lançar uma exceção personalizada `NotaInvalidaError`. O bloco `try-except` deve
# capturar e tratar essa exceção. Dica: Você pode verificar se a nota é int ou float com a função
# `isinstance(nota, (int, float)) `.

import statistics as sta

class NotaInvalidaError(Exception):
    pass


def calcular_media(notas):
    try:
        for nota in notas:
            if not isinstance(nota, (int,float)):
                raise NotaInvalidaError('ERRO: a lista possui um valor invalido')
        media = sta.mean(notas)
        return media
    
    except NotaInvalidaError as N:
            print(N)
            
notas = [5,7,'ponto']
media = calcular_media(notas)
print(media)
        
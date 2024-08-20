#Exercício 2: Cálculo de Médias Ponderadas
# Desenvolva uma função chamada calcular_medias que receba uma lista de
# listas, onde cada sublista contém três notas de um aluno. A função deve
# calcular a média ponderada de cada aluno, considerando pesos de 30%
# para as duas primeiras notas e 40% para a terceira nota.
# Retorne uma lista com as médias calculadas e imprima as notas dos alunos
# junto com as respectivas médias.

def calcular_medias(lista_notas):

    medias = []
    
    for notas in lista_notas:
        n1, n2, n3 = notas

        media_ponderada = (n1 * 0.30) + (n2 * 0.30) + (n3 * 0.40)

        medias.append(media_ponderada)
        
        print(f'Notas: {notas} => Média Ponderada: {media_ponderada:.2f}')
    
    return medias


lista_notas = [
    [5.5, 8.5, 9.5],
    [2.5, 6.0, 7.5],
    [9.0, 3.0, 6.5]
]

medias = calcular_medias(lista_notas)

# Escreva uma função chamada intercala_numeros que recebe como entrada duas listas
# de três elementos e retorna uma lista de seis elementos, com os números intercalados.
# Exemplo: Suponha que as listas de entrada da função sejam:
# [1, 2, 3]
# [4, 5, 6]
# Para estas listas, a função deve retornar:
# [1, 4, 2, 5, 3, 6]

def intercala_numeros(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista

lista1 = []
lista2 = []

for i in range (3):
    num = int(input('insira os numeros da lista 1: '))
    lista1.append(num)

for i in range (3):
    num = int(input('insira os numeros da lista 2: '))
    lista2.append(num)


print(intercala_numeros(lista1,lista2))

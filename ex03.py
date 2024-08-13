#Exercício 3: Remoção de Números Pares
# Implemente uma função chamada remover_pares que receba uma lista de
# números inteiros e retorne uma nova lista contendo apenas os números
# ímpares. Utilize um loop for para percorrer a lista e verifique se cada
# número é ímpar. Por fim, imprima a lista original e a lista resultante
# com os números ímpares.

lista = [51,65,34,148,2585,14,69,25,35,14,970,64,354,19]
impar = []
def remover_pares(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            impar.append(i)
            return impar

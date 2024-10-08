##Exercício 4: Exercício de Controle Manual de Arquivo
##Crie um programa que abra um arquivo de texto chamado controle.txt,
##escreva uma linha e depois feche manualmente o arquivo (usando open e close).
##Em seguida, reabra o arquivo e leia o conteúdo.

f = open('controle.txt', 'w')
f.write('Arquivo do exercicio 4!\n')
f.close()

with open('controle.txt', 'r') as f:
    print(f.read())
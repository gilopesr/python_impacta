##Exercício 1: Manipulação de Arquivos de Texto Simples
##Crie um programa em Python que escreva cinco frases em um arquivo de texto chamado mensagens.txt.
##Em seguida, leia e exiba o conteúdo do arquivo.

f = open('ex001.txt', 'a')
f.write('aprendendo a manipular arquivos!\n')
f.close()

f = open('ex001.txt', 'a')
f.write('aula de programação orientada a objetos\n')
f.close()

f = open('ex001.txt', 'a')
f.write('olá mundo!\n')
f.close()

f = open('ex001.txt', 'a')
f.write('everglow forever lets go!\n')
f.close()

f = open('ex001.txt', 'a')
f.write('txt 4gen it group\n')
f.close()
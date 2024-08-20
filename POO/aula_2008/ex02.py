# Preencha um dicionário com os dados de 5 alunos
# - Utilize o ra do aluno como chave e uma lista de três notas como valor.
# - Solicite os dados do usuário
# - Percorra o dicionário e exiba a média de cada aluno.
# Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]}

dadosAlunos = {}

while len(dadosAlunos) < 5:
    listaNotas = []
    RA = input(f'insira o ra do aluno: ')

    for i in range(3):
        nota = float(input('insira a sua nota: '))
        listaNotas.append(nota)

    dadosAlunos[RA] = listaNotas

for chave, valor in dadosAlunos.items():
    print(f'RA: {chave}')
    print(f'Notas:{valor}')
    print(f'Média: {(sum(valor))/len(valor):.2f}')
    print(20*'-')
    
##Exercício 3: Manipulação de Arquivos JSON
##Crie um programa que crie um arquivo dados.json, contendo as informações de um livro: título, autor e ano de
##publicação. O programa deve salvar os dados no formato JSON e, em seguida, ler e exibir o conteúdo.

import json

dados = {
    'livro' : [
        {
            'titulo' : 'Harry Potter e o Prisioneiro de Azkaban',
            'autor' : 'JK Rowling',
            'ano de publicacao' : '08/07/1999',
        },
        {
            'titulo' : 'Coraline',
            'autor' : 'Neil Gaiman',
            'ano de publicacao' : '02/07/2002',
        }
    ]
}


dados_str = json.dumps(dados, indent=2)
print(dados_str)
with open ('dados.json', 'w') as f:
    json.dump(dados, f, indent=2)

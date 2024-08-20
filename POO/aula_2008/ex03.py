# Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
# quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade
# de vezes que essa vogal aparece no texto.
# A função deve receber o texto como entrada e retornar o dicionário.
# Exemplo:
# Para o texto abaixo:
# texto = &#39; faculdade impacta de tecnologia&#39;
# A função deve devolver o seguinte dicionário:
# {&#39;a&#39;: 5, &#39;u&#39;: 1, &#39;e&#39;: 3, &#39;o&#39; : 2, &#39;i&#39;: 2 }

def conta_vogais(string):
    string = string.lower()
    contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for i in string:
        if i in contagem_vogais:
            contagem_vogais[i] += 1
    return contagem_vogais


texto = str(input('insira um texto/frase para saber a quantidade de vogais que ele possui: '))
print(f'o texto possui a seguinte quantidade de vogais: {conta_vogais(texto)}')

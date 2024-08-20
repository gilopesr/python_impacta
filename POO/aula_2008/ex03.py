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
    resultado = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            resultado[i] = string.count(i)
            return resultado

print(conta_vogais('faculdade impacta de tecnologia'))
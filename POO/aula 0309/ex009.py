# Exercício 9: Composição

# Crie uma classe Sala e uma classe Edificio. Um edifício deve
# conter várias salas, e a existência das salas deve depender da
# existência do edifício. Se o edifício for destruído, suas salas
# também serão.

# Defina a classe Sala com um atributo numero.
# Defina a classe Edificio com um atributo para armazenar uma
# lista de Salas.
# No construtor do Edificio, crie as Salas internamente.
# No exemplo de uso, crie um edifício e observe que as salas são
# criadas como parte do edifício.

class Sala:
    def __init__(self, numero):
        self.numero = numero

class Edificio:
    def __init__(self, qntd_salas):
        self.lista_salas = [Sala(numero) for numero in range(1,qntd_salas+1)]


ed = Edificio(5) 

for sala in ed.lista_salas:
    print(f'sala num: {sala.numero}')

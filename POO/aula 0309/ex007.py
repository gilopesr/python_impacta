# Exercício 7: Dependência

# Crie uma classe Mensagem e uma classe Correio. A classe
# Correio deve ter um método que envia uma Mensagem. A
# relação entre Correio e Mensagem deve ser uma dependência.

# • Defina a classe Mensagem com um atributo texto.
# • Defina a classe Correio com um método enviar que aceita
# um objeto Mensagem como parâmetro e imprime o texto da
# mensagem.
# • No exemplo de uso, crie uma mensagem e use o correio para
# enviá-la.

class Correio:
    def enviar_mensagem (self, mensagem):
        print(f'enviando a carta: {mensagem}')

class Mensagem:
    def escrever_texto (self,correio, texto):
        correio.enviar_mensagem(texto)

correio = Correio()
mensagem = Mensagem()
mensagem.escrever_texto(correio, 'olá amiga, escrevo esta carta......')

# 7. Agendamento de Eventos
# Descrição: Implemente uma classe Evento com atributos para
# nome do evento, data e número de participantes. Adicione
# métodos para alterar a data do evento e outro para exibir as
# informações do evento.
import datetime

class Evento:
    def __init__(self, nome_evento, data, num_participantes):
        self.nome_evento = nome_evento
        self.data = data
        self.num_participantes = num_participantes
    
    def MudarData(self, data_nova):
        self.data = data_nova
        print('Atenção com a data nova!')

    def info(self):
        print(f'Nome do Evento: {self.nome_evento}')
        print(f'Data: {self.data}')
        print(f'Numero de Participantes: {self.num_participantes}')
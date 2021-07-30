"""
Manipulando Data e Hora

Python tem um módulo buit-in (integrado) para se trabalhar com data e hora
chamado datetime

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Dentro da classe datetime
print(datetime.datetime.now())  # 2021-07-30 20:08:48.108489
print(repr(datetime.datetime.now()))  # representação

# método replace() para fazer ajustes
inicio = datetime.datetime.now()
print(inicio)

#alterando
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# declarando
evento = datetime.datetime(2021, 1, 23, 17, 0, 0, 0)
print(type(evento))
print(evento)

# exemplo
data_nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
data_nascimento = data_nascimento.split('/')

hora_nascimento = input('Informe que horas vc nasceu (hh:mm): ')
hora_nascimento = hora_nascimento.split(':')

nascimento = datetime.datetime(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]), int(hora_nascimento[0]), int(hora_nascimento[1]))
print(nascimento)  # 1998-01-09 22:04:00
"""

import datetime

# Acessando elementos

evento = datetime.datetime(2021, 1, 23, 17, 4, 13, 1)

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

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
"""

import datetime

# declarando
evento = datetime.datetime(2021, 1, 23, 17, 0, 0, 0)
print(type(evento))
print(evento)

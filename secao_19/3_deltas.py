"""
Trabalhando com deltas de data e hora
"""

import datetime

hoje = datetime.datetime.now()
evento = datetime.datetime(2020, 11, 18)  # te amo

tempo_para_evento = evento - hoje

print(type(tempo_para_evento))
print(tempo_para_evento)

print(f'Já se passaram {-tempo_para_evento.days} dias que eu te beijei pela primeira vez!')

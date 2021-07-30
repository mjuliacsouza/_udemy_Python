"""
Métodos de data e hora

import datetime

agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# mesmo resultado, porém o now() pode ser especificado por uma time zone

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar dia da semana, weeekday()

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao.weekday())  # em números

# 0: segunda-feira
# 1: terça-feira
# 2: quarta-feira
# 3: quinta-feira
# 4: sexta-feira
# 5: sábado
# 6: domingo


aniversario = input('Informe sua data de nascimento (dd/mm/yyyy): ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

dias_da_semana = {'segunda-feira': 0,
                  'terça-feira': 1,
                  'quarta-feira': 2,
                  'quinta-feira': 3,
                  'sexta-feira': 4,
                  'sábado':5,
                  'domingo': 6}

for key, value in dias_da_semana.items():
    if aniversario.weekday() == value:
        print(f'Você nasceu em {key}')
"""

import datetime

# formatando

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # se usar %y fica apenas dois numero
print(hoje_formatado)

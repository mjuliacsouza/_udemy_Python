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

from textblob import TextBlob

# formatando

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # se usar %y fica apenas dois numero
print(hoje_formatado)

hoje_formatado = hoje.strftime('%B %d, %Y')  # nome do mês em ingles
print(hoje_formatado)

print(TextBlob(hoje.strftime('%B')).translate(to='pt-br'))  # traduz para pt

# Transformando string em datetime

nascimento = datetime.datetime.strptime('07/11/1997', '%d/%m/%Y')
print(nascimento)
print(type(nascimento))
print(repr(nascimento))

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)
"""

import timeit

# Tempo de execuçao

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)  # 0.2858718

# List comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)  # 0.22382919999999995

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)  # 0.19083889999999992

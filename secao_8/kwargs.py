"""
Entendendo o **kwargs

- Indicado apenas pelo duplo asterisco **, o nome 'kwargs' é apenas uma convenção

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em
uma tupla, o **kwargs exige que utilizemos parâmetro nomeados (chave/valor) e transforma
esses parâmetros extras em um dicionário.

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')


cores_favoritas(marcos='verde', julia='amarelo', fernando='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.


Nas nossas funções, podemos ter (NESTA ORDEM):

    - Parâmetros obrigatórios
    - *args
    - Parâmetros default
    - **kwargs

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome': 'Felciity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))
"""


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

# OBS: os nomes da chave no dicionário devem ser os mesmos da função

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

"""
Assertions (Checagens ou questionamentos)

Em Python, utiliza-se a palavra resevada 'assert' para realizar testes
em expressões nos testes.

# OBS: pode-se especificar opcionalmente um segunto argumento e uma mensagem
de error personalizada.
"""


def soma_numero_positivos(a, b):
    assert a>0 and b>0, 'Ambos números precisam ser positivos'
    return a + b

# ret = soma_numero_positivos(-2, 4)
ret = soma_numero_positivos(2, 4)
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'hamburguer',
        'esfiha'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


ret = comer_fast_food(input('Informe sua comida: '))
print(ret)

# se for executado com parâetro -O, nenhum assertion será validado

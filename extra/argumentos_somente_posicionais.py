"""
Argumentos somente posicionais
"""

valor = "67.3"
print(float(valor))
# print(floar(x=valor)) # não funciona


def cumprimenta_v1(nome):
    return f'Olá {nome}!'


print(cumprimenta_v1('Julia'))
print(cumprimenta_v1(nome='Julia'))


def cumprimenta_v2(nome, /):  # antes
    return f'Olá {nome}!'


print(cumprimenta_v2('Julia'))
# print(cumprimenta_v2(nome='Julia'))  # erro, argumento apenas posicional antes


def cumprimenta_v3(*, nome):  # depois
    return f'Olá {nome}!'


print(cumprimenta_v3('Julia'))
# print(cumprimenta_v3(nome='Julia')) # erro, argumento apenas posicional depois

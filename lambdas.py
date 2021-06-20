"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas são funções sem nome, ou seja, funções anônimas.

# Função em Python:


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar?
calc = lambda x: 3 * x + 1

print(calc(4))
"""

# Podemos ter expressões lambda com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip.title() + ' ' + sobrenome.strip.title()

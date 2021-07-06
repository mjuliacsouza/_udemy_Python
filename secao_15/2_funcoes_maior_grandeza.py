"""
Funções de maior grandeza - Higher Order Funcitions (HOF)

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter
funções que retornam outras funções como resultado ou mesmo que podemos
passar funções como argumentos para outras funções e até mesmo criar variáveis
do tipo de funções nos nossos programas.

OBS: Na seção de funções, foram utilizadas.

Em Python, as funções são Cidadões de Primeira Classe (First Class Citizen)

# Exemplo - definindo funções


def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 2, soma))
print(calcular(4, 2, diminuir))
print(calcular(4, 2, multiplicar))
print(calcular(4, 2, dividir))


# Nested Function (Funções aninhadas)


Em Python, podemos ter funções dentro de funções (inner functions).

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(["E ai? ", "Saia daqui, ", "Gosto muito de você, "])
    return humor() + pessoa


# Testando

print(cumprimento('Mariano'))
print(cumprimento('Angela'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(['hahahaha', 'kkkkkkkkkk', 'yayayayaya'])
    return rir


# Testando

rindo = faz_me_rir()
print(rindo())
"""

# Inner Function podem acessar o escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(['hahahahaha', 'kkkkkkkkk', 'yayayayaya'])
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernando')

print(rindo())
print(rindo())
print(rindo())

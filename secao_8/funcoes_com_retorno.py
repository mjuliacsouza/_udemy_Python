"""
Funções com retorno

# Exemplo função sem retorno


def quadrado_de_7():
    print(7*7)


ret = quadrado_de_7()
print(ret)  # None

# Exemplo função com retorno


def quadrado_de_7():
    resultado = 7*7
    return resultado


# Para retornar usa-se a palavra reservada 'return'
print(quadrado_de_7())

OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, retornar qualquer tipo de dado e até multiplos valores

# Exemplo 1


def diz_oi():
    print('é executada')
    return 'oi'
    #print('Depois do return')  # Não será executada


print(diz_oi())

# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
"""

# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

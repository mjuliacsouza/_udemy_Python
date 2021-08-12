"""
Tipos de dados mais precisos


def dobro(numero: int) -> int:
    return numero * 2


print(dobro(3))
# print(dobro('Geek'))  # é executado

A versão mais nova do Python tem novos tipos de dados:
    - Literal type
    - Union
    - Final
    - Typed dictionaries
    - Protocols

# Literal type

from typing import Literal


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


# a saída deve ser obrigatoriamente 'conectado' ou 'desconectado'
"""

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)  # 10
calcula_v1('-', 6, 4)  # 2
calcula_v1('*', 6, 4)  # ValueError

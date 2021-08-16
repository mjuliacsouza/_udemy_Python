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


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v2('+', 6, 4)  # 10
calcula_v2('-', 6, 4)  # 2
calcula_v2('*', 6, 4)  # ValueError

from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande...'
    else:
        return resultado

from typing import Final

NOME: Final = "Geek"

print(NOME)

NOME = 'University'  # erro

print(NOME)


from typing import final


@final
class Pessoa:
    pass


class Estudante(Pessoa):  # não poderia acontecer pois Pessoa é final
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):  # não poderia acontecer pois estudar de estudante é final
        print('Estudando e estagiando....')

# Dá erro

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)

outro = CursoPython(algo='vai', coisa=True)  # erro
print(outro)

# Todos os erros são detectados com mypy
"""

# Protocols



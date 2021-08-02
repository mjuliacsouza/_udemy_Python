"""
DocTests

São testes que colocamos em docstrings das funções/métodos Python.
"""


def soma(a, b):
    """soma os número a e b

    >>> soma(1, 2)
    3
    """
    return a + b


# print(soma(2, 4))  # 6

# Aplicando o TDD


def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    lista = [2 * elemento for elemento in valores]
    return lista


print(duplicar([1, 1, 1]))

# Erro inesperado


def fala_oi():
    """fala oi

    >>> fala_oi()
    'oi'
    """
    return 'oi'

# colocar aspas simples dentro das aspas duplas

# Último exemplo


def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

# print(cabecalho('geek university', alinhamento=12))

print(cabecalho.__annotations__)

"""
Instalar mypy:

pip install mypy

Executando no terminal:

mypy my_py.py

O mypy mostrará o erro da linha 12:

my_py.py:12: error: Argument "alinhamento" to "cabecalho" has incompatible type "int
"; expected "bool"

Found 1 error in 1 file (checked 1 source file)

Caso a linha 12 esteja comentada:

Success: no issues found in 1 source file
"""

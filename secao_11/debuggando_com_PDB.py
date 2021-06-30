"""
Debuggando com PCB

PDB -> Python Debugger

# OBS: a utilizando do print para debuggar é uma prática ruim


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug com o debugger
# Em Python, podemos fazer isso com diferentes IDE's ou utilizando o PDB

# Utilizando o PyCharm

def dividir(a, b):  # breakpoint
    try:
        return int(a)/int(b)  # breakpoint, dá pra colocar a divizão no 'watches'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))
# Mostram o quanto está valendo cada variável e outras dicas

# Utilizando o PDB - Exemplo 1

# Para utilizar o PDB, precisamos importar uma biblioteca e utilizar a função set_trace()

# Comando básicos do PDB:
# l (listas onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução)

import pdb

nome = "Angelina"
sobrenome = "Jolie"

pdb.set_trace()  # breakpoint

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Utilizando PDB - Exemplo 2

nome = "Angelina"
sobrenome = "Jolie"

import pdb; pdb.set_trace()  # breakpoint

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

#    Por que utilizar esse formato? O Debug é utilzado durante o desenvolvimento,
# costumamos realizar todos os imports de bibliotecas no começo do arquivo. Por
# isso, as invés de colocarmos o import no início, colocamos somente onde vamos u
# utilziar, e, ao finalizar, removemos.

# Utilizando PDB - Exemplo 3

# * A partir do python 3.7 não é mais necessário importar a biblioteca, o comandoi
# foi incorporado como função integrada, chamada breakpoint()

nome = "Angelina"
sobrenome = "Jolie"

breakpoint()  # funciona da mesma forma

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# OBS: Cuidado com conflitos entre nomes de variáveis e os comando do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# como as variáveis tem o mesmo nome dos comando, ao chamar a variável no
# debugger, será executado o comando, teremos que usar p: nome_da_variável

# Evitar esses nomes não representativos

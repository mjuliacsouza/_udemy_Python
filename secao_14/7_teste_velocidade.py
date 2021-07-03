"""
Teste de Velocidade com Expressões Geradoras

# Generators


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # generator
print(next(ge1))  # 1
print(next(ge1))  # 2
print(next(ge1))  # 3

# Generator Expressions

ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))  # 1
print(next(ge2))  # 2
print(next(ge2))  # 3
"""

# Realizando Teste de Velocidade
import time

# Generator Expressions
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')

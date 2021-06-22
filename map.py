"""
Map

Com Map fazemos mapeamento de valores para função

import math


def area(r):
    '''Calcula a área de um círculo com raio r'''
    return math.pi * (r ** 2)


print(area(2))

raios = [2, 5, 7.1, 7.3, 44]

# forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - com MAP

# Map é uma função que recebe dois parâmetros: a função e um iterável

areas = map(area, raios)
print(list(areas))

# Forma 3 - map com lambda
print(list(map(lambda r: math.pi * r ** 2, raios)))

# OBS: Após utilizar a função MAP, depois da primeira utilização do resultado, ele zero.
# Map recebe apenas um parâmetro
"""

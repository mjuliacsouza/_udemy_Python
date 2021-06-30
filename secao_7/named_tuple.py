""""
Módulo collections - Named Tuple

# Revisão tupla

tupla = (1, 2, 3)
print(tupla[0])

Named tuple -> são tuplas diferenciadas onde especificamos um nome para a
mesma e parâmetros
"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e os parâmetros

# Declarando
# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-chow', nome='Ray')

print(ray)

# os outros métodos de tuplas são válidos aqui

# Acessando os dados - diferente
print(ray.raca)
print(ray.nome)
print(ray.idade)

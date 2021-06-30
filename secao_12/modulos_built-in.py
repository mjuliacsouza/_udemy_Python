"""
Trabalhando com módulos built-in (integrados)

# Utilizando alias (apelidos) para módulos/funções

import random as rdn

print(rdn.random())

# Podemos importar todas as funções e módulos com *

from random import *

print(random())

# Importando todo o módulo

import random
print(random.random())

# Utilizando alias para módulos/funções

from random import randint as rdi

print(rdi(1, 3))

# Costuma-se utilizar tuple para colocar multiplos imports
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(0, 3))

lista = [1, 2, 3, 4]
shuffle(lista)

print(lista)
print(choice(lista))
"""

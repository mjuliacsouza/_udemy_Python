""""
Módulo Collections - Ordered Dict

Dicionários não são ordenados.

Ordered Dict é um dicionário que garante a ordem de inserção dos elementos.

# Importando
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c':3})

for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')
"""

from collections import OrderedDict

# Entendendo a diferença

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)   # True, já que a ordem dos elementos não importa

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False, já que a ordem importa

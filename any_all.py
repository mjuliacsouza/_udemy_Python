"""
Any e All

All: retorna True se todos os elementos do iteravel são verdadeiros ou se o iteravel está vazio

# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Todos são True? Não, o zero é falso
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True

OBS: não apenas listas, mas sets, tuplas também.

nomes = ['Carla', 'Carolina', 'Celio', 'Carlos', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))  # True

Any: Retorna True se qualquer elemento de iterável for verdadeiro, se o iterável estiver vaio,
retorn Falso
"""

# Exemplo any()
print(any([0, 1, 2, 3, 4]))  # Pelo menos um é verdadeiro, assim: True
print(any([0, False, {}, ()]))  # False, tudo é falso
print(any([]))  # False

nomes = ['Carla', 'Carolina', 'Celio', 'Carlos', 'Cristina', 'Ana']
print(any([nome[0] == 'C' for nome in nomes]))  # True

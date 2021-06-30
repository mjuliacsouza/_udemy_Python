"""
Generator Expression

Em aulas anteriores vimos list, dict e set comprehension, mas não vimos
set comprehension ,isso é porque se chamam generators.

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))  # True

# Isso não é um list comprehension, como havia sido feito anteriormente

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)  # Geral uma lista

# Generator
res = (nome[0] == 'C' for nome in nomes)  # Não é uma tupla!
print(type(res))
print(res)  # Gera um objeto em memória

# Generator ocupa menos recurso em memória!

# Para retorna a quantidade de bytes em memória
from sys import getsizeof

print('string: "Geek", bytes: ',getsizeof('Geek'))  # String
print('string: "Geek University", bytes: ', getsizeof('Geek University'))  # String
print('int: 3, bytes: ', getsizeof(3))  # int
print('int: 3000000000, bytes: ', getsizeof(300000000))  # int
print('bool: True, bytes: ', getsizeof(True))  # Boolean
print('bool: False, bytes: ', getsizeof(False))  # Boolean

# List comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Para generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa, gastamos:')
print(f'List Comp: {list_comp} bytes')  # 8856
print(f'Set Comp: {set_comp} bytes')  # 32984
print(f'Dict Comp: {dict_comp} bytes \n ')  # 36960
print('Enquanto:')
print(f'Generator Expression: {gen} bytes')  # 112

# Valor bem menor
"""

# Podemos iterar no Generator Expression

gen = (x * 10 for x in range(10))
print(gen)
print(type(gen))

for num in gen:
    print(num)

"""
Reversed

OBS: Não confunda com a função reverse() das listas

A função Reversed funciona para todos os iteráveis, enquanto reverse() apenas para listas.
Sua função é inverter o iterável.
"""

# Exemplos

lista = [1, 2, 3, 4]
print(lista)

res = reversed(lista)
print(res)  # é um objeto
print(type(res))

print(list(res))
print(list(res))  # só retorna na primeira vez
print(lista)  # não altera a lista original

print(set(reversed(lista)))  # em set não definimos a ordem dos elementos
print(tuple(reversed(lista)))  # em tupla podemos definir a ordem

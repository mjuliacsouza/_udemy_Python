"""
Set comprehension
"""

# Exemplos

# 1

numeros = {num for num in range(1, 7)}
print(numeros)

# 2

numeros = {x ** 2 for x in range(10)}
print(numeros)

# 3
letras = {letra for letra in "Geek University"}
print(letras)

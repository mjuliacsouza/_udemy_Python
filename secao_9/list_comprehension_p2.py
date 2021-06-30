"""
List Comprehension (2)

Nós podemos adicionar estruturas condicionais l[ogicas às nossas list comprehesion
"""

# Exmeplos

# 1

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# para o Python: 0 é False
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

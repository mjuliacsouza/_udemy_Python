"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrtura de dados chamadas
de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensional (Matrizes)

Em Python nós temos as listas.
"""

# Exemplos

# Matriz 3 x 3
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
print(listas)
print(type(listas))

# Como fazemos pra acessar os dados?

# Acessamos a primeira lista, ou seja, a primeira linha da matriz
print(listas[0])

# Acessamos o primeiro elemento da primeira lista,  ou seja, o elemento
# da primeira coluna e primeira linha
print(listas[0][0])

# Iterando com loops em uma linha aninhada
for lista in listas:
    for elemento in lista:
        print(elemento)

# List comprehension

[[print(valor) for valor in lista] for lista in listas]
"""

# Outros exemplos

# Gerando um tabuleiro/matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

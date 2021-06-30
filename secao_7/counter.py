"""
Módulo collection - Counter

Collection -> High-performance container Datatypes

Counter -> recebe um iterável como parâmetro e cria um objeto do tipo
Collection counter que é parecido com um dicionário, contendo chave, o
elemento da lista passado como parâmetro e o como valor a quantidade de
ocorrências desse elemento.

# Importando o Counter

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 6, 5, 5, 45, 12, 34, 98, 22]

# Utilizando o Conter

# A partir de uma lista
res = Counter(lista)
print(res)
print(type(res))

# A partir de uma string
print(Counter('Geek University'))
"""

from collections import Counter

# Exemplo 3 - Linguagem Natural

texto = """Nonbinary (also spelled non-binary) means any gender 
identity that is not strictly male or female all the time, and so 
does not fit within the gender binary. For some people, "nonbinary" 
is as specific as they want to get about labeling their gender. 
For others, they call themselves a more specific gender identity 
under the nonbinary umbrella. Many people who call themselves 
nonbinary also consider themselves genderqueer. However, the terms 
have different meanings and connotations: genderqueer means any 
gender identity or expression which is, itself, queer."""

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# As 5 palavras com mais ocorrência
print(res.most_common(5))

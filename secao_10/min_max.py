"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou entre dois ou mais elementos

min() -> Retorna o menor valor em um iteravel ou entre dois ou mais elementos

# Exemplos MAX e MIN

lista = [1, 290, 3, 78, 2, 0.6]
print(max(lista))  # 290
print(min(lista))  # 0.6

set1 = {1, 290, 3, 78, 2, 0.6}
print(max(set1))  # 290
print(min(set1))  # 0.6

tupla = (1, 290, 3, 78, 2, 0.6)
print(max(tupla))  # 290
print(min(tupla))  # 0.6

el1 = 1
el2 = 200
el3 = 44
print(max(el1, el2, el3))  # 200
print(min(el1, el2, el3))  # 1

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(max(dicionario))  # f
print(min(dicionario))  # a
print(max(dicionario.values()))  # 6
print(min(dicionario.values()))  # 1
"""

# Outros exemplos

nomes = ['Arya', 'Sansom', 'Dara', 'Tim', 'Ollyvandir']

# Vai considerar a ordem alfabética
print(max(nomes))
print(min(nomes))

# Considerar tamanho
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

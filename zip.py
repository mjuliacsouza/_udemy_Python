"""
Zip

zip() -> Cria um interavel (zp object) que agrega elemento de cada um dos iteraveis
de entrada.

# Exemplo

lista1 = [1, 2, 3, 10]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)  # cria tuplas com os elementos, o valor 10 será ignorado

print(zip1)
print(type(zip1))
print(list(zip1))  # pode ser set, tupla e dict também, só pode ser chamado uma vez
# retorna: [(1, 4), (2, 5), (3, 6)]

zip1 = zip(lista1, lista2)
print(dict(zip1))  # aqui a primeira lista vira a chave e a segundo o valor

# Utilizando elementos diferentes
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zp = zip(tupla, lista, dicionario.values())
print(list(zp))

# Lista de tuplas
dados = [(0, 1), (2, 3), (4,5)]
print(list(zip(*dados)))
"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos usar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

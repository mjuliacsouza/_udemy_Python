"""
Sorted

OBS: não confunda com a função sort() de listas

Podemos utilizar o sorted com qualquer interável, diferente do sort que
só funciona com listas.

# Exemplos

numeros = [1, 4, 2, 8, 4]  # se fosse uma tupla aqui o sorted retorna sempre uma lista
print(numeros)

print(sorted(numeros))
print(numeros)  # a lista não se altera, diferente do sort que modifica a lista

# Adicionando parâmetros ao sorted
print(sorted(numeros, reverse=True))
print(tuple(sorted(numeros, reverse=True)))
print(set(sorted(numeros, reverse=True)))

# Podemos utiliza-lo para coisas mais complexas

usuarios = [
    {'user_name': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'user_name': 'carla', 'tweets': ['Eu adoro carros'], 'cor': 'preto'},
    {'user_name': 'jeff', 'tweets': [], 'cor': 'amarelo', 'musica': 'indie'},
    {'user_name': 'bob123', 'tweets': ['Eu amo meu cachorro', 'Eu to com fome']},
    {'user_name': 'jane', 'tweets': []}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario['user_name']))  # ordem alfabética
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))  # numero de tweets
"""

# Ultimo exemplo
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 2},
    {'titulo': 'Tears in Heaven', 'tocou': 30},
    {'titulo': 'Chicago', 'tocou': 9},
    {'titulo': '1950', 'tocou': 1},
]

# Ordena da mais tocada para menos
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

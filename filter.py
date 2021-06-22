"""
Filter

Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando mean():
media = statistics.mean(dados)

# OBS: Assim como em MAP, o FILTER recebe dois parâmetros, uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

# Depois de imprimir a primeira vez o res fica vazio
print(f'Segunda vez: {list(res)}')

paises = ['', 'Argentine', '', 'Brasil', 'Chile', '', '', 'Venezuela']

res = filter(None, paises)  # exclui os dados vazios
print(list(res))

# A diferença entre MAP e FILTER é:

# Map() -> Recebe dois parâmetro (funçao e iteravel) e retorna um objeto mapeando a funçao para cada iteravel
# Filter() -> Recebe os mesmos dois parâmetros mas retorna um objeto filtrando apenas os objetos de acordo com a funçao

# Exemplos mais complexos

usuarios = [
    {'user_name': 'samuel', 'tweets':['Eu adoro bolos', 'Eu adoro pizzas']},
    {'user_name': 'carla', 'tweets':['Eu adoro carros']},
    {'user_name': 'jeff', 'tweets':[]},
    {'user_name': 'bob123', 'tweets':['Eu amo meu cachorro', 'Eu to com fome']},
    {'user_name': 'jane', 'tweets':[]}
]

# Filtrar os usuários que estão inativos no Twitter:

#inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
"""

# Combinar FILTER e MAP

nomes = ['Vanessa', 'Ana', 'Maria']

# Criar uma lista contendo "Sua instrutora é" + nome, desde que nome tenha menos de 5 caracteres
ret = list(map(lambda nome: f"Sua instrutora é {nome}",
               filter(lambda nome: len(nome) < 5, nomes)))
print(ret)

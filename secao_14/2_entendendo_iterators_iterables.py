"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamda
Iterable ->
    - Um objeto que irá retornar um iterador quando a função iter() for chamada

# São iterables mas não não iterators
nome = 'Gekk'
numeros = [1, 2, 3, 4, 5, 6, 7]

# print(next(numeros)) # dá erro pois list não é iterator
# print(next(nome)) # dá erro pois str não é iterator

# Criando iterators a partir dos iterables
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it2))

# OBS: só funciona com os elementos existentes nos iterators

nome = 'geek'

for letra in nome:
    # por debaixo dos panos o nome está sendo transformado em iterator
    print(f'{letra}')
"""

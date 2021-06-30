"""
Len, Abs, Sum, Round

# Len

len() - > Retorna o tamanho (numero de itesn) de um iteravel.

# Exemplo len()
print(len('Geek Universisty'))
print(len([1, 2, 3]))
print(len((1, 2, 3)))
print(len({1, 2, 3}))
print(len({'a': 1, 'b': 2, 'c':3}))

# Por debaixo dos panos, ao utilizar len() o Python faz:
print('Geek Universisty'.__len__())  # dunder len

# Abs

abs() -> retorna o valor absoluta de um numero inteiro ou real, de forma básica, tira o sinal

# Exemplo abs()
print(abs(-3))
print(abs(-3.14))
print(abs(3))
print(abs(3.14))
#print(abs('oi'))  # não pode, dá TypeError

# Sum

sum() -> recebe como parâmetro um iteravel, podendo receber um valor inicial e
retorna a soma total incluindo o valor inicial. Valor inicial defalut é 0.

# Exemplo de sum()
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))  # adiciona o 5 à soma dos iteraveis
print(sum((1, 2, 3, 4, 5)))  # funciona com tupla
print(sum({1, 2, 3, 4, 5}))  # funciona com set
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))  # funciona os valores de um dict
# print(sum('Geek'))  # não funciona com strings

# Round

round() -> Retorna um numero arredondado para o digito de precisão após a casa decima
o valor default é o inteiro mais próximo.
"""

# Exemplos de round()
print(round(4.5))
print(round(4.6))
print(round(4.4))
print(round(4.5446, 2))

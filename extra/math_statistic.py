"""
Novas ferramentas de matemática e estatística
"""

# math.prod --> retorna o produto de um container numérico

import math
nums_1 = [2, 3, 7, 9]
nums_2 = {2, 3, 7, 9}
nums_3 = (2, 3, 7, 9)

print(math.prod(nums_1))
print(math.prod(nums_2))
print(math.prod(nums_3))

# math.isqrt --> devolve a parte inteira

print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))

# math.dist --> distancia entre pontos

p1 = [12, 50, 2]  # tem que ser um container
p2 = [4, 90, 1]

print(math.dist(p1, p2))

# math.hypot --> hipotenusa ou norma euclidiana

print(math.hypot(*p1))  # para descompactar o container
print(math.hypot(*p2))

import statistics

# statistics.fmean --> média de numeros reais

valores_reais = [1.45, 5.89, 2.74]
valores_inteiros = [1, 6, 3]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean -> calcula a média geométrica de numeros reais

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode -> retorna o valor mais frequente numa sequência

seq1 = 'Geek University'
seq2 = [3, 5, 9, 5, 4, 2, 5, 6, 5]  # 3
seq3 = [1, 5, 2, 8, 1, 9, 1, 2, 1, 2, 2]  # 1 e 2

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))


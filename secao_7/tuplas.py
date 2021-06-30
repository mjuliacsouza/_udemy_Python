"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas. Existem basicamente
duas diferenças básicas:

    I - Tuplas são representadas por parênteses: ()

    II - As tuplas são imutáveis, isso significa que ao se criar
uma tupla, ela não muda, toda operação numa tupla gera uma nova tupla

# CUIDADO I: tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Ambas são tuplas

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)   #isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4, # isso é uma tupla
print(tupla5)
print(type(tupla5))

#ou seja, tupla são definidas pelas vírgulas e não pelos ()

# Podemos geral uma tupla com o range a partir de tuple()
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ("Geek University", "Programação em Python: Essencial",)

escola, curso = tupla
print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem
pois as tuplas são imutáveis.

# Soma, valor máximo, valor mínimo e tamanho podem se os valores forem todos inteiros ou reais.

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis mas podemos sobreescrever
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = "Geek University"
escola = tuple(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos numa coleção

# Exemplo 1

meses = ("Janeiro", "Fevereiro", "Março", "Abril",
         "Maio", "Junho", "Julho", "Agosto", "Setembro",
         "Outubro", "Novembro", "Dezembro")
# meses.append("Outono") #dá erro
print(meses)

# O acesso de elementos de uma tupla também é semelhante à de uma lista
print(meses[5])

# Iterar com 'while'
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar em qual índice um elemento está na tupla

print(meses.index("Outubro"))

# OBS: Caso o elemento não exista, teremos ValueError

# Se tiver mais de uma vez, retorna a primeira ocorrência

# Slicing
# tupla[início:fim:passo]

print(meses[0:])

# Por quê utilizar Tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais segura (imutabilidade).

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)
"""

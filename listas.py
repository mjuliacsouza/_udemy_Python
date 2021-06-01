"""
Listas

Listas em python funcionam como vetores ou matrizes (arrays), com a
diferença de serem dinâmicos e também de podermos colocar QUALQUER
tipo de dado

Linguagens C/Java: Arrays
    -Possuem tamanho e tipo de dado fixo;

Linguagem Python:
    - Dinâmico
    - Qualquer tipo de dado

As listas em python são representadas por colchetes: []
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', 'U', 'n', 'i', 'v', 'e', 'r']
lista3 = []
lista4 = list(range(11))
lista5 = list("Geek University")

"""
# Podemos facilmente checar se determinado valor está contido na lista
num = 8
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print("Não encontrei")

# Podemos facilmente ordenar uma lista
print(f"antes de ordenar: {lista1}")
lista1.sort()
print(f'depois de ordenar: {lista1}')

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

'''
Para adicionar elementos em listas, utilizamos a função append

OBS: com append, só conseguimos add um elemento por vez
lista1.append(1, 2) # ERRO
'''
print(lista1)
lista1.append(42)
print(lista1)
lista1.append([1, 2])    # Coloca a lista como elemento único
print(lista1)

if [1, 2] in lista1:
    print("Encontrei")
else:
    print("Não encontrei")

lista1.extend([2, 3])    # Coloca cada elemento de uma lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: não substitui o valor da posição indicada, é deslocado
lista1.insert(2, "novo valor")
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Podemos inverter uma lista

# FORMA 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# FORMA 2
print(lista1[::-1])
print(lista2[::-1])

# Podemos facilmente copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos saber o tamanho de uma lista, quantos elementos tem
print(len(lista3))

# Podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)
print(lista5.pop())  #Não só remove mas também retorna o último elemento
print(lista5)

#Podemos remover o elemento pelo índice
# OBS: elementos à direita são deslocados para esquerda
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exmeplo 1

curso = "Programação  em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, a split separa os elementos da lista pelo espaço entre elas.
curso = "Programação,em,Python:,Essencial"
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação','em','Python:','Essencial']
print(lista6)
curso = ' '.join(lista6)  # Pode ser qualquer separador
print(curso)

# Iterando sobre listas

# Exeplo 1 - utilizando for
for elemento in lista1:
    print(elemento)

#Exemplo 2 - Utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista oui digite sair para sair: ')
    produto = input()
    if produto !='sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numero = [1, 2, 3]

num1 = 1
num2 = 2
num3 = 3
numeros = [num1, num2, num3]

# Fazemos acesso aos elementos de forma indexada
cores=['verde','amarelo', 'azul', 'branco']
print(cores[1])    #amarelo

# Fazer acesso aos elementos de forma inversa
cores=['verde','amarelo', 'azul', 'branco']
print(cores[-1])         #branco

# Geral índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10,5]
print(numeros.index(6))

# OBS: caso não tenha esse elemento na lista, será apresentado erro
print(numeros.index(5))    #retorna a primeira ocorrência

print(numeros.index(5,1,7))     # indica um ponto de partida e ponto final

# Revisão de Slicing
# lista[inicio:fim:passo]

# Invertendo valores de uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Soma, valor máximo, mínimo, tamanho
# (com valores inteiros ou reais)
lista = [1, 2, 3, 4]
print(sum(lista))
print(min(lista))
print(max(lista))
print(len(lista))

# Transformar uma lista em tupla
lista = [1, 2, 3, 4]
print(type(lista))
tupla = tuple(lista)
print(type(tupla))

# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1, num2, num3)
#OBS: se tivermos mais elementos que variáveis, teremos erro

# Copia de listas (Shallow e Deep Copies)

# Forma 1 # É o Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizar lista.copy, copiamos os dados mas as lista ficaram independentes

# Forma 2 (Shallow Copy)
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)
nova.append(4)

print(lista)
print(nova)
"""

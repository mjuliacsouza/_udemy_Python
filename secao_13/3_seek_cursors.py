"""
Seek e Cursors

seek() -> utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt', encoding='utf-8')

print('Primeira vez: ', arquivo.read(), end='\n\n')
print('Segunda vez: ', arquivo.read(), end='\n\n')  # não faz nada

# Movimentando o cursos pelo arquivo:

arquivo.seek(0)  # movimentamos o cursor para a posição zero
print('Após movimentar o cursor: ', arquivo.read(), end='\n\n')  # agora vemos o texto e novo

# Podemos reposicionar o cursor em qualquer ponto do texto.

arquivo = open('texto.txt', encoding='utf-8')

# readline() -> Lendo o arquivo linha a linha

print(arquivo.readline(), end='\n')
print(arquivo.readline(), end='\n')
print(arquivo.readline(), end='\n')  # o arquivo só tem três linhas

# lembrando que o retorno dessas função são string, tanto o read() quanto o readline()
# assim, podemos utilizar todas as funções de uma string

arquivo = open('texto.txt', encoding='utf-8')

# readlines() -> ler um conjunto de linhas com uma lista das linhas

print(arquivo.readlines())
"""

# Obs: quando abrimos um arquivo com open() é criada uma conexão entre o arquivo
# no disco e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
# os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos o
# close()

# Passos:

# 1 - Abrir o arquivo
arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)  # verifica se o arquivo esta aberto ou fechado

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)

# print(arquivo.read()) # teremos ValueError, pois está fechado

# OBS: se vc colocar um número n como argumento do read(n) ele vai imprimir os n caracteres

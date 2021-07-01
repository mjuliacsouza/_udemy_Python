"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, usamos a função integrada open().

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro
de entrada, que neste caso é o nome do arquivo a ser lido. Essa função retorna
um _io_TextIOWrapper e é com ele que travalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve
existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode: 'r' -> Modo de leitura (read)

"""

# Exemplo

arquivo = open('texto.txt', encoding="utf-8")

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo após sua abertura,
# devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos
# chamado cursor. Esse cursos funciona como o cursos quando
# estamos escrevendo.

print(arquivo.read())  # ele não vai imprimir nada

# OBS: a função read() lê todo o conteúdo do arquivo

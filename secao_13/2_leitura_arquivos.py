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

arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))

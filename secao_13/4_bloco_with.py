"""
O bloco with

Passos para trabalhar com arquivos

1 - Abrir o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with
"""

# O bloco with

with open('texto.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())

# aqui o arquivo já está fechado
print(arquivo.closed)  # True

"""
Módulo collections - Default Dict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # dá erro

Default Dict -> ao criar um dicionário utilizando-o, nós informamos um
valor default podendo utilizar um lambda para isso. este valor será
utilizado sempre que não houver um valor definido. Caso tenemos acessa
uma chave que não existe, essa chave será criada e o valor default será
atribuído.

# OBS: Lambda são funções sem nome que podem ou não receber parâmetros de
entrada e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])  # valor default
print(dicionario)

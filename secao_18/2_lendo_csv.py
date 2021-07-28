"""
Lendo arquivos CSV

CSV - Comma Separated Values

import pandas as pd

lutadores = pd.read_csv('lutadores.csv')
print(lutadores)

with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    print(type(dados))
    # dados = dados.split(',')
    print(dados)

A linguagem Python tem duas formas de ler csv:
    - reader -> Permite que iteremos sobre as linhas do arquivo csv como linhas
    - DiscReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDict

# Reader

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} cm.')
"""

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} cm.")

"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas função para utilizarmos
Pacote -> É um diretório contendo uma coleção de módulos

OBS: Nas versoes 2.X do Python, um pacote Python deveria conter dentro dele
um arquivo chamado __init__.py

Nas versões mais novas, não é obrigatório mas ainda é utilizado para manter
compatibilidade.

Criei um pacote 'test' com test1 e test2 e um subpacote 'subtest' com test3 e test4
"""

from test import test1, test2
from test.subtest import test3, test4

print(test1.pi)
print(test1.funcao1(4, 6))

print(test2.curso)
print(test2.funcao2())

print(test3.funcao3())

print(test4.funcao4())

"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes
# e propriedades que estão dentro do módulo ficarão em memória.

print(random.random())

# random() -> Gera um semi-aleatorio entre 0 e 1

# Forma 2 - importando função específica (forma recomendada)

from random import random

print(random())  # funciona da mesma forma

# uniform -> Gerar um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluido

# randint() -> Gera valores pseudo-aleatório entre os valores estabelecidos

from random import randint

# Gerador de apostas

for i in range(6):
    print(randint(1, 6), end=', ')  # inclui 1 e 6, com repetição

# choice() -> Mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cartas)
shuffle(cartas)
print(cartas)

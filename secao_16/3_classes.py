"""
POO - Classes

Classes, nada mais são, do que modelos dos objetos do mundo real sendo
representados computacionalmente.

Classes podem conter:
    - Atributos => Representam as características do objeto

    - Métodos (funções) => Representam os comportamentos do objeto, as
    ações que podem realizar no sistema

Em Python, para definir uma classe utilizamos uma palavra reservada 'class'.

Quando nomeamos uma classe em Python, utilizamos por convenção uma inicial em maiucula.
"""


class Lampada:
    pass  # para ignorar


# ao criar a classe, cria-se um tipo de dado
lamp = Lampada()
print(type(lamp))

# os inteiros também são uma classe (interna do Python)
numero = int('42')
print(type(numero))

# classes internas do Python foram criadas em minúsculo
# Objetos mapeados pela classe são entidades

"""
POO - Métodos

- Métodos (funções) => Representam os comportamentos dos objetos, ou seja,
as ações que estes objetos podem realizar no seu sistema.

Em Python, dividimos em Métodos de Instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método construtor e sua função é
construir um objeto atraves da classe.

# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self._voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return(f'O valor com desconto é R$ {self.__valor * (100 - porcentagem) / 100}.')


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def __correr__(self, metros):  # é recomendado nunca criar esse tipo de método
        print(f'{self.__nome} está correndo {metros} metros.')


melissa = Usuario('Melissa', 'melissinha@gamil.com', 'monsterhigh123')
melissa.__correr__(34)

ps4 = Produto ("Playstation 4", 'Video-game', 2300)
print(ps4.desconto(20))

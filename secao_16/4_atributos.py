"""
POO - Atributos

Atributos são usados para representar computacionalmente os estados
de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos.

# Atributos de instância: São atributos declarados dentro do método construtor

# OBS: métodos construtor é um método especial utilizado para a construção do
objeto.
"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = f'R$ {valor},00'


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


ps4 = Produto('Playstation 4', 'Console de videogame', 3000)
print(ps4)
print(ps4.nome)
print(ps4.descricao)
print(ps4.valor)

# a palavra self é conveção, a primeira palavra de atributo do __init__ sempre será o self

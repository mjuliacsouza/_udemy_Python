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
# atributos privados só podem ser utilizados dentro da própria classe de definição
# enquanto os atributos públicos podem ser utilizados por todos

# Em Python, por convenção, todo atributo de uma classe é público (pode ser acessado
# em todo o projeto), para ser dito como privado utiliza-se Name Mangling (__)


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


acessando = Acesso('user@gmail.com', '12345')
print(acessando.email)  # atributo público
# print(acessando.senha)  # atributo privado, vai dar erro

# print(acessando._Acesso__senha)  # aqui você consegue ter acesso, Name Mangling#

# O que significa Atributos de Instância?

# Ao criarmos instâncias/objetos de uma classe, todas as instâncias terão
# estes atributos.


# Atributos de Classe
p1 = Produto('Playstation 4', 'Video-game', 2300)
p2 = Produto('XBox S', 'Video-game', 4500)

# São atributos que são declarados diretamente na classe, fora do cosntrutor
# geralmente já inicializamos um valor que é compartilhado entre todas as
# instâncias.
"""

# Refotorando a classe produto:


class Produto:

    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = f'R$ {str(valor * Produto.imposto).replace(".",",")}'
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video-game', 2300)
p2 = Produto('XBox S', 'Video-game', 4500)

print(p1.valor)
print(p2.valor)

print(Produto.imposto)  # acessando atributo de classe

print(p1.id)  # 1
print(p2.id)  # 2

print(Produto.contador)  # terá o valor da última instância implementada, 2

# Em Java, atributos de classe são atributos estáticos

# Atributos Dinâmicos

# Atributos de instância que pode ser criado em tempo de execução
# Será exclusivo da instância que o criou

p3 = Produto('Arroz', 'Comida', 5.5)
p3.peso = '5 kg'

p4 = Produto('Feijão', 'Comida', 8)

print(p3.peso)
# print(p4.peso) # Atribute Error

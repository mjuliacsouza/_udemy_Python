"""
POO - Herança Múltipla

Herança Múltipla é a possiblidade de ter herança de múltiplas classes, onde a
classe filha herda todas as classes e métodos de todas as classes herdadas.

Pode ser feita de duas maneiras:
    - Multuiderivação direta
    - Multiderivação indireta

# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação indireta


class Base11:
    pass


class Base12(Base11):
    pass


class MultiDerivada2(Base12):
    pass

# Não importa se é indireta ou direta, a classe que herdar, herdará todos os atributos e métodos
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou{self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xin')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar())  # ??? Method resolution Order - MRO

# Objeto é instância de outro objeto?

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')

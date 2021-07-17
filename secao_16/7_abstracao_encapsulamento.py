"""
POO - Abstração e Encapsulamento

O grande objetivo do POO é encapsular nosso código dentro de um grupo
lógico e hierárquico utilizando classes.
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def estrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser positivo')

    def sacar(self, valor):
        if valor >= 0 & self.__saldo >= valor:
            self.__saldo -= valor
        elif valor < 0:
            print('Valor precisa ser positivo')
        elif self.__saldo < valor:
            print('Saldo insuficiente')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


conta1 = Conta('Julia', 1600, 20000)

conta1.estrato()
conta1.depositar(-150)
conta1.estrato()
conta1.sacar(200)
conta1.estrato()
conta1.sacar(2200)
conta1.estrato()

conta2 = Conta('Nicolas', 0, 500)

conta1.transferir(500, conta2)

conta1.estrato()
conta2.estrato()

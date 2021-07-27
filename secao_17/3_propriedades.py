"""
POO - Propriedades (Properties)

Em linguagens de programação como o Java, ao declararmos atributos
privados nas classes, costumamos criar métodos publicos para a maipulação
desses atributos. Esses métodos são conhecidos como getters e setters.


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Nicolas', 2000, 10000)
conta2 = Conta('Julia', 5000, 50000)

print(conta1.extrato())
print(conta2.extrato())

# soma = conta1._Conta__saldo + conta2._Conta__saldo  # não é correto
# print(soma)

soma2 = conta1.get_saldo() + conta2.get_saldo()  # forma correta
print(soma2)

print(conta1.__dict__)
conta1.set_limite(9999999)
print(conta1.__dict__)
"""

# Refatorando utilizando propriedades


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Nicolas', 2000, 10000)
conta2 = Conta('Julia', 5000, 50000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos das contas é: {soma}')

print(conta1.__dict__)
conta1.limite = 9999999
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)

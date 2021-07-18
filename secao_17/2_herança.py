"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também estender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós estendemos outra
classe que passa a herdar atributos e métodos da classe herdada.

Existe uma entidade genérica o suficiente para encapsular os atributos?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Amanda', 'Teodócia', '123.456.789-00', 5000)
funcionario1 = Funcionario('Mikaela', 'Strauss', '69.6969.6969-42', 6969)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Refatorando


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf,  renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


# Quando uma classe herda de outra, ela herda todos os atributos e métodos.
# A classe herdada é a Super Classe, Classe Mae, Pai ou Classa Base.
# A classe que herda são sub classes, classe filha ou específica.

cliente1 = Cliente('Amanda', 'Teodócia', '123.456.789-00', 5000)
funcionario1 = Funcionario('Mikaela', 'Strauss', '69.6969.6969-42', 6969)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
"""

# Sobreescrita de Métodos (Overriding)

# Ocorre quando reescrevemos um métodos da super classe na classe filha


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf,  renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente = Cliente('Amanda', 'Teodócia', '123.456.789-00', 5000)
funcionario = Funcionario('Mikaela', 'Strauss', '69.6969.6969-42', 6969)

print(cliente.nome_completo())
print(funcionario.nome_completo())

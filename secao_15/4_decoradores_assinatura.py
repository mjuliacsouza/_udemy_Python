"""
Decorators com diferentes assinaturas

# As vezes, utilizamos um padrão de projeto chamado Decorator Pattern
"""


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou ê {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao("Otávio"))
print(ordernar('Picanha', 'Batata frita'))

# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros
# de entrada.

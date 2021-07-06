"""
Decorators com diferentes assinaturas

# As vezes, utilizamos um padrão de projeto chamado Decorator Pattern


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

# OBS: vale lembrar que podemos utilizar parâmetros nomeados

print(ordernar(acompanhamento='Batata Frita', principal='Picanha'))
"""

# Decorators com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# testando

print(soma_dez(10, 12))  # 22
print(soma_dez(1, 21))  # Valor incorreto, primeiro tem que ser 10

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'churrasco'))  # primeiro tem que ser pizza

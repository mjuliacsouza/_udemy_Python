"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas são funções sem nome, ou seja, funções anônimas.

# Função em Python:


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar?
calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambda com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip.title() + ' ' + sobrenome.strip.title()

# Em funções Python podemos ter nenhuma ouv árias entradas, em Lambdas também?

amar = lambda: "como não amar python"

uma = lambda x: 3 * x + 1

duas = lambda x, y: x + y*3

print(amar())
print(uma(6))
print(duas(3, 4))

# se passar mais argumentos que parâmetros teremos TypeError

autores = ['Isaac Asimov', 'Ray Bradbury', 'C. S. Lewis', 'Arthur C. Clarke']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# definindo função


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a* x**2 + b*x + c """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))

print(geradora_funcao_quadratica(3, 0, 1)(2))
"""

# Aplicações: filtragem de dados

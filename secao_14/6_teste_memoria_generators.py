"""
Teste de Memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34, 55 etc

# Função com listas 449 MB


def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste
for n in fib_lista(100000):
    print(n)
"""

# Função com geradores 3MB


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


# Teste 2
for n in fib_gen(100000):
    print(n)

# Geradores ocupam bem menos memória

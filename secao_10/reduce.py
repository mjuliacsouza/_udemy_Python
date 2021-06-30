"""
Reduce

OBS: A partir do Python 3 e acima, a função Reduce não é mais uma função
integrada, deve-se utilizar um módulo.

Na maioria das vezes é mais simples utilizar loop for.

Para entender o Reduce:
    - Imagine que vc tem uma coleção de dados
    - E você tem uma função que recebe dois parâmetros
    - A função Reduce funciona de forma:

dados = [a1, a2, a3, a4,..., a5]
def funcao(x, y):
    resultado = f(x, y)
    return resultado

Assim como map() e filter(), o reduce() recebe dois parâmetros: a funçao e o iteravel

reduce(funcao, dados)

    1. Primeiro Passo: res1 = f(a1, a2) # Aplica a funçao nos dois primeiros elementos e guarda o resultado
    2. Segundo Passo: res2 = f(res1, a3) # Aplica a funçao no resultado do passo 1 mais o terceiro elementos e guarda o resultado
    3. Terceiro Passo: res3 = f(res2, a4)
    etc
    n. Ultimo Passo: resN = f(resN-1, an)

Repetido até o final dos dados.
"""

# Exemplos

# Vamos utilizar a função para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 7, 11, 23, 19, 26, 5]
multi = lambda x, y: x * y

res = reduce(multi, dados)  # Ele retorna os dados diretamente
print(res)
print(res)  # Guarda os valores por mais tempo que map() e filter()

# Utilizando um loop

res = 1
for n in dados:
    res = res * n
print(res)

"""
Entendendo *args

- O *args é um parâmetro de entrada da função, isso significa que poderá ter
qualquer nome se iniciado por asterisco (*).

O parâmetro *args utilizado em uma função coloca os valores extras informados
como entrada em uma tupla (imutáveis).

# exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

# TypeError
# print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(3, 4, 5, 6))
"""

# entendendo o *args


def soma_todos_numeros(*args):
    total = 0
    for num in args:
        total = total + num
    return total


print(soma_todos_numeros(2))
print(soma_todos_numeros(2, 4))
print(soma_todos_numeros(2, 4, 5))

# OBS: O asterisco serva para informar ao Python que estamos passando
# como argumento uma coleção de dados. Dessa forma, ele saberá que
# precisará antes desempacotar estes dados.
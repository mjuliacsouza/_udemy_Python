"""
Funções com parãmetro

 - Funções que recebem dados para serem processados dentro da mesma

Se a gente passar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

# Refatorando uma função


def quadrado_de_7():
    return 7*7


print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())  # sempre dá o mesmo resultado


def quadrado(numero):
    return numero*numero


print(quadrado(5))
print(quadrado(6))
print(quadrado(7))  # se eu não der o parâmetro, vai dar TypeError

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# de uma função quantos parâmetros forem necessários, separados por vírgula.

# Exemplo


def soma(a, b):
    return a+b


print(soma(1, 2))

# Diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declardas na definição da função
# Argumentos sao dados passado durante a execução da função

# A ordem dos parâmetros importa!

def nome_completo(nome, sobrenome):
    print(f'Seu nome é {nome} {sobrenome}.')


nome_completo(sobrenome='Souza', nome='Nicolas')
"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

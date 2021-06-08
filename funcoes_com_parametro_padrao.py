"""
Funções com parâmetro padrão (default parameters)

- Funções onde a passagem de parâmetros seja opcional

# Exemplo de parâmetro opcional
print('Geek University')
print()  # sem erro

# Exemplo de parâmetro obrigatório
def quadrado(numero):
    return numero**2

print(quadrado())  # TypeError

# Refatoração


def exponencial(numero, potencia=2):  # coloca potencia com valor padrão
    return numero**potencia


print(exponencial(3))  # vai usar potencial=2 como padrão

# OBS: Em funções Pyhton, os parâmetros com valores default DEVEM sempre estar
# ao final da declaraçao


# Qualquer tipo de dado pode ser utilizado como valor default

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = "Python"  # variável local
    return f'oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local de mesmo nome de uma global,
# ela terá preferência

def diz_oi():
    prof = 'geek'
    return f'Olá {prof}'

print(diz_oi())
print(prof)  # NameError

# ATENÇÃO com variável globais (se puder evitar, evite)

total = 0


def incrementa():
    total = total + 1
    return total


print(incrementa())  # dá erro pois variável total não foi inicializada dentro da função

# Podemos usar:
total = 0


def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
print(incrementa())  # estamos mudando a variável global
"""

# Podemos ter funções declaradas dentro de funções e uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())  # sempre dá 1

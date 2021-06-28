"""
Try/ Except/ Else/ Finally

Dica de quando e onde tratar código:
    - TODA ENTRADA DEVE SER TRATADA

# Else -> é executado apenas se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}.')

# Finally -> é sempre executado, ocorrendo exceçao ou não

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}.')
finally:
    print('Executando finally')

# OBS: é utilizado geralmente para fechar ou desalocar recursos (Banco de Dados)

# Exemplo mais complexo - tratar erros na função:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo - tratamento genérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""

# Exemplo - tratamento semi-genérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

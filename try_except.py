"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso
código, prevenindo, assim, que o programa pare de funcionar e o usuário receba
mensagens de erros inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando erro genérico

#geek()  # NameError

try:
    geek()
except:
    print('Deu algum problema')

# Exemplo 2 - Tratando erro genérico (typeerror)

try:
    len(5)
except:
    print('Deu algum problema')

# Exemplo 3 - Tratando erro específico

try:
    geek()
except NameError:
    print('Você está usando função inexistente')

# Exemplo 4 - Tratando erro específico

try:
    len(5)  # como isso não é NameError, mas TypeError, não entra no except
except NameError:
    print('Você está usando função inexistente')

# Exemplo 5 - Erro espcífico

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")

try:
    # len(5)
    # geek()
    print('Geek'[9])
except NameError as errA:
    print(f'Deu NameError: {errA}')
except TypeError as errB:
    print(f'Deu TypeError: {errB}')
except:
    print(f'Deu um erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}
print(pega_valor(dic, 'game'))
print(pega_valor(dic, 80))

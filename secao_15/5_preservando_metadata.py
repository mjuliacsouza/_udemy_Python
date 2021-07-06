"""
Preservando metadatas com wraps

Metadatas -> são dados intrínsecos nos arquivos.
Wraps -> são funcoes que envolvem elementos com diversas finalidades.

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra (como doc)
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui a documentação {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #soma dois numeros (como doc)
    return f'Resultado: {a + b}'

# print(soma(1, 1))  # 2

print(soma.__name__)  # logar
print(soma.__doc__)  # doc de logar

# A partir do momento que é feito a decoração de uma função, o metadata dela
# é alterado para o decarator relacionado.
"""

# Resolução
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui a documentação {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """soma dois numeros"""
    return f'Resultado: {a + b}'


# print(soma(1, 1))  # funciona da mesma forma

print(soma.__name__)  # soma
print(soma.__doc__)  # doc de soma

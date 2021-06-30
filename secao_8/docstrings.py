"""
Documentando funções com docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando
o método especial __doc__.

Podemos ainda fazer acesso à documentação com a função help
"""

# Exemplo


def diz_oi():
    """Um função simples que retorna a string 'Oi'"""
    return 'Oi'


# se vc fazer o import desse arquivo e funçõa e pedir 'help(diz_oi)', imprimirá
# o texto escrito


def exponencial(numero, potencia=2):
    """
    Função que retonra por padrão o quadrado do numero ou 'numero' à 'potencia' informada
    :param numero: numero que desejamos geral a potencia
    :param potencia: potencia que queremos, por padrão é pois
    :return: retorna o exponencial do numero
    """
    return numero**potencia

"""
Forçando tipos de dados com decoradores
"""


def forcao_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Geek'), int('3')
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forcao_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')


@forcao_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 3)

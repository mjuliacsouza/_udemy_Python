"""
Levantando os prórpios erros com raise

raise -> Lança exceções, não é uma função, é uma palavra reservada.

Para simplificar, pense no raise como sendo útil para criar nossas próprias
exceções e mensagens de erro.

Forma geral de utilização:

    raise TipoDoErro('mensagem do erro')

# Exemplo 1


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')  # não é exceçao
colore('Geek', 4)  # cor não é string

# Exemplo 2


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Palavra', 'verde')  # dá certo
colore('Palavra', 'roxo')  # roxo não está na lista

# OBS: o raise finaliza a função, como o return, nada depois após do raise é executado
"""

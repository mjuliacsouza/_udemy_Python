"""
Erros mais comuns em Python

- Prestar a tenção na saída de erros

Os erros mais comuns:

- SyntaxeError -> Ocorre quando o Python encontra um erro de sintaxe, ou
seja, você escreveu algo que o Python não reconhece como parte da linguagem.

    EX:
    a)
    def funcao:
        print('oi')

    b)
    None = 1  # palavra reservada

    c)
    return

- NameError -> Ocorre quando uma variável ou função não foi definida.

    EX:
    a)
    print(geek)  # nome geek não foi definido

    b)
    geek()  # função não definida

- TypeError -> Ocorre quando uma função/operação/ação é aplicada à um tipo
errado.

    EX:
    a)
    print(len(5))

    b)
    print('Geek' + [])

- IndexError -> Ocorre quando tentamos acessar um elementos em uma lista ou
outro tipo de dado indexado utilizando um índice inválido.

    EX:
    a)
    lista = ['Um']
    print(lista[1])  # lista só tem posição 0
    print(lista[0][2]  # palavra só tem duas letras

- ValueError -> Ocorre quando uma função/operação built-in recebe um argumento
com tipo correto mas valor inapropriado.

    EX:
    a)
    print(int('Geek'))  # a função 'int' aceitaria '1', ou qualquer str de numero

- KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que
não existe.

    EX:
    dict = {'oi': 45}
    print(dict['tchau'])  # não tem essa chave no dicionário

- AtributeError -> Ocorre quando uma variável não tem um atributo/função.

    EX:
    tupla = (11, 2, 31, 4)
    print(tupla.sort())  # a função 'sort()' é de listas não tuplas

- IndentationError -> Ocorre quando não respeitamos a identação do Python, que
é de 4 espaços.

    EX:
    def nova()
     return 'oi'  # foi dado apenas um espaço

Esses são os error principais, temos muito mais.
OBS: Exceptions e Errors são sinônimos na programação.
"""

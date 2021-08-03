def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

# print(cabecalho('geek university', alinhamento=1))  # usa como True, não dá erro

'''
Podemos colocar o tipo num comentário também, que nem abaixo:

def cabecalho(texto, alinhamento: bool = True):
    # type: (str) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')
'''
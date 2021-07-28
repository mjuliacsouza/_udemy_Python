"""
POO - Métodos Mágicos

São todos os métodos que utilizam Dunder (__).

dunder repr -> representação do objeto
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # sem isso, ao fazer print do objeto ele retorna o endereço
        return self.titulo  # sobreescrevendo a classe object

    ''' 
    # Faz o mesmo que o __repr__
    def __str__(self):
        return self.titulo
    '''

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória.')

    def __add__(self, outro):
        return f'{self} - {outro}'


livro1 = Livro('1984', 'George Orwell', 350)
livro2 = Livro('Revolução dos Bixos', 'George Orwell', 150)

print(livro1)
print(livro2)  # titulo dos livros

print(len(livro1))
print(len(livro2))  # numero de paginas

print(livro1 + livro2)

# Eu não sei porque está imprimindo a saida do método '__del__'

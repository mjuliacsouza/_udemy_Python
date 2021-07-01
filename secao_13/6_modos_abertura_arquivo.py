"""
Modos de abertura de Arquivo

r -> Abre para leitura - padrao
w -> Abre para escrita - sobreescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso exista, gera FileExistError

try:
    with open('texto.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('TEste de conteúdo. \n')
except FileExistsError:
    print('Arquivo já existe')

a -> Abre para escrita, adicionando ao final do arquivo caso exista
"""

with open('fruta.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informa uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write('- ' + fruta.capitalize() + '\n')
        else:
            break

with open('fruta.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())

# OBS: com o modo 'a' não controlamos o cursor, se colocarmos 'a+' e 'r+' teremos novas funcionalidades
# ai o cursor sempre retorna pro começo depois de ler o arquivo todo

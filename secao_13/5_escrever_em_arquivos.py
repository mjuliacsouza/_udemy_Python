"""
Escrevendo em arquivos

Vamos utilizar outro modo de abertura da função open(), antes utilizamvamos o
modo 'r', que era somente para leitura, não podendo realizar escrita nele. Agora,
podemos utilizar o modo para escrita, não podendo lê-lo.

# Modo de leitura

with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Este é um novo arquivo \n')
    arquivo.write('Escrever dados em arquivo é muito fácil \n')
    arquivo.write('Podemos colocar várias linhas')

# aqui foi criado um novo arquivo chamado 'novo' com o texto especificado
# se fosse colocado em um arquivo antigo, seria sobre-escrito, perdendo o que se tinha

with open('novo.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())

# Truques de str

with open('patodavida.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Textinho pro amor da minha vida, acho que ela nunca vai encontrar, mas está aqui. \n')
    arquivo.write('TE AMO ' * 1000)

with open('patodavida.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())
"""

with open('fruta.txt', 'w', encoding='utf=8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write("- " + fruta.capitalize() + '\n')
        else:
            break
with open('fruta.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())

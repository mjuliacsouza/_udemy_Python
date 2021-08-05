"""
Operador Walrus

Permite fazer a tribuição e retorno de valor em uma única expressão.

variável := expressão
"""

# Exemplo 1

# print(nome)  # 'nome' is not defined
print(nome := 'Geek University')
print(nome)

# Exemplo 2

# Python até 3.7
cesta =[]
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')
print(cesta)

# Python a partir de 3.8
cesta2 = []
while(fruta2 := input('Informe a fruta: ')) != 'jaca':
    cesta2.append(fruta2)
print(cesta2)

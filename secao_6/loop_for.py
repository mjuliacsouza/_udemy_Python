"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

# C ou Java

for (int i = 0; i < limitador; i++){
    //execução ou loop
}

# Python

for item in iteravel:
    //execução de loop

Utilizamos loops para iterar sobre sequêncuias ou sobre iteráveis

Exemplo de iteraveis:
    - String
    - Lista
    - Range
"""

'''
# Exemplos

# Exemplo de for 1 (Iterando uma string)
print("Exemplo 1")
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
print("Exemplo 2")
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
print("Exemplo 3")
for numero in range(1,10):
    print(numero)
'''

'''
# Enumerate

for i, v in enumerate(nome):
    print(nome[i])

for i, v in enumerate(nome):
    print(v)

for _, letra in enumerate(nome):
    print(letra)
    
OBS: Quando não precisamos de um valor, podemos descartá-lo com un underline (_)

for valor in enumerate(nome):
    print(valor[0])

OBS: Assimt emos uma tupla
'''

'''
# Usando input 

qtd = int(input("Quantas vezes esse loop deve rodar?"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')
'''

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

'''
Tabela Unicode Emojis: https://apps.timwhitlock.info/emoji/tables/unicode
'''

# Original: U+1F633
# Modificado: U0001F633

for num in range(1,11):
    print('\U0001F633' * num)

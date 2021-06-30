"""
Mapas -> conhecidos em Python como dicionários

Dicionários em python são representados por chaves

receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)

#Iterar sobre dicionários

# Imprimindo as chaves
for chave in receita:
    print(chave)

# Imprimindo os valores
for chave in receita:
    print(receita[chave])

# Os dois
for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Método keys
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

print(receita.items())

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""

receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)

# Soma, valor máximo, mínimo e tamnanho
# Se os valores foram int ou float

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

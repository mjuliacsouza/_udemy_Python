"""
Dicionários

OBS: em algumas linguagens de programação, os dicionários Python
são conhecidos por mapas.

Dicionários são coleções de tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários:
    - Chaves e valor são separados por dois ponto 'chave':'valor'
    - Tanto chave quando valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

# Criação de dicionários

# Forma 1: Mais comum
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))

#Forma 2: Menos comum
paises=dict(br='Brasil', eua='estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1: Acessando via chave da mesma forma que lista/tupla

print(paises['br'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe,
teremos um KeyError

# Forma 2: Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))  # Não dá erro, retorna 'None'

# Tipo None: representa o tipo 'sem tipo' ou vazio. Sempre especificado com a
primeira letra maiúscula. Utilizando quando
    - Queremos criar uma variável e iniciáliza-la com um tipo 'sem tipo'
    antes de recebermos um valor final.
# OBS: O tipo None em Python é sempre considerado como False.

# O método get é recomendado por não dar KeyError com valores não existentes
no dicionário.

# Outras funcionalidades do get.

pais = paises.get('ru', 'Não encontrado')   # Caso não encontre o objeto com essa chave, ele coloca esse valor
print(pais)


# Ver se tem essa chave no dict:

print('br' in paises)
print('ru' in paises)

# Podemos utilizar qualquer tipo de dado (int, string, boolean), inclusive lista, tupla, como chave de dicionário

# Tuplas são interessantes como chaves por ser imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório de Tókio',
    (48.7128, 74.0060): 'Escritório em Nova York'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2 - mais comum
novo_dados = {'mai': 500}
receita.update(novo_dados)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550

# Forma 2
receita.update({'mai':600})
print(receita)

# CONCLUSÃO 1: a forma de adicionar novos elementos ou atuliazar dados é a mesma
# CONCLUSAO 2: em dicionário NÃO podemos ter chaves repetida


# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - mais comum
ret = receita.pop('mar')
print(ret)
print(receita)

#OBS: aqui precisamos informar a chave e caso não encontre dá KeyError
#OBS 2: ao removermos o elemento, ele é retornável

# Forma 2
del receita['fev']
print(receita)

# Se tentar remover novamente dá KeyError
# OBS: nesse caso o valor removido não é retornável

# Imagine que vc tem um comércio eletrônico onde temos um carrinho de compras no qual adicionamos produtos.

'''
Carrinho de Compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço
    Prduto 2:
        - nome 
        - quantidade
        - preço
'''
# Poderíamos utilizar uma lista para isso, mas teríamos que saber q ual o índice de
# cada informação do produto. Com uma tupla não poderíamos atualizar o carrinho. Com
# o dicionário podemos atualizar valores e também chamar os valores facilmente.

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep copy
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow copy
novo = d
print(novo)
novo['d'] = 4
print(novo)
print(d)

# Forma não usual de criação de dicionários

outros = {}.fromkeys('a', 'b')
print(outros)
print(type(outros))

usuario = {}.fromkeys(['nome', 'pontos', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método 'fromkeys' recebe dois valores, um iterável e um valor.
# Cad iteravel vira uma chave e o valor será dado a todas as chaves.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
"""

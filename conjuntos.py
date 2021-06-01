"""
Conjuntos

- Conjuntos em linguagem de programação, estamos fazendo referência
a teoria de conjuntos da matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
    - Sets não possuem valores duplicados;
    - Sets não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, não são indexados.

Conjuntos são bons para se armazenar elementos, mas sem
se preocupar com a ordenação deles. Quando não precisamos
se preocupar com chaves, valores e items duplicados.

Os conjuntos são referênciados em Python com chaves {}

Diferenças entre Sets e Mapas em Python:
    - Um dicionário tem chave/valor.
    - Um conjunto tem apenas valor.

# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que há valores repetidos
print(s)
print(type(s))

# OBS: ao criar um conjunto, caso seja adicionado um valor repetidos, será ignorando.

# Forma 2 - mais comum

s = {1, 2, 3, 4, 5, 6, 6}
print(s)
print(type(s))

 # Podemos gerar um set a partir de:
    - String
    - Lista
    - tupla

# Podemos verificar se tem dado elementos:
if 3 in set:
    print('tem 3')
else:
    print('não tem')

# Não é ordenado nem aceita duplicado

dados = '2265199120'

lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturado em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes e esses informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas temos
print(len(set(cidades)))

# Adicionando elementos em um conjunto (eles são mutáveis)
s = {1, 2, 3}

s.add(4)
s.add(4)  # não gera erro, apenas é ignorado
print(s)

# Remover elementos
s = {1, 2, 3}

# Forma 1
s.remove(1)  # informa-se o valor
print(s)

#s.remove(7)  # causa erro quando o valor não é encotrado

# Forma 2
s.discard(2)
s.discard(2)  # não causa erro
print(s)

# OBS: esses métodos não retornam o valor removido

# Copiando um conjunto
s = {1, 2, 3}
print(s)

# Forma 1 - Deep copy
nova = s.copy()
nova.add(4)
print(s)
print(nova)

# Forma 2 - Shallow copy
novo = s
novo.add(4)
print(s)
print(novo)

s = {1, 2, 3}
print(s)

# Podemos remoer todos os itens

s.clear()
print(s)

# Métodos matemáticos de conjunto

# Imagine que temos dois conjuntos.
# um primeiros com estudantes de Python
# Um segundo com estudantes de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos estudam as duas linguagens

# Precisamos de um conjuntos com todos os estudantes

# Forma 1 - utilizando Union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
print(type(unicos1))

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
print(type(unicos2))

# Gerar um conjunto de estudantes em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando &

ambos2 = estudantes_python & estudantes_java
print(ambos2)
print(type(ambos2))

# Gerar o contrário do anterior
soh_python = estudantes_python.difference(estudantes_java)
print(soh_python)

soh_java = estudantes_java.difference(estudantes_python)
print(soh_java)
"""

# Soma, valor máximo, mínimo e tamanho
# Todos int e/ou float

s = {1, 2, 3, 4, 5}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

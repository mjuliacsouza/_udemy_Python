"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

RAnges são utilizados para gerar sequências numéricas, não de forma aleatória
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão em 0 e passo de 1 em 1)

# Exemplo Forma 1
print("Exemplo forma 1")
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_porada)

# Exmeplo forma 2
print("Exmeplo forma 2")
for num in range(1,11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

# Exmeplo Forma 3
print("Exemplo forma 3")
for num in range(1, 10, 2):
    print(num)

# Forma 4

range(valor_final, valor_inicio, passo_negativo)

# Exemplo Forma 4
print("exemplo forma 4")
for num in range(10, 0, -1):
    print(num)

"""

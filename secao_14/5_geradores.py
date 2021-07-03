"""
Geradores

- Geradores (Generators) são Iterators (Iteradores)
- Nem todo Iterator é um Generator

Outros:
    - Generators podem ser criado com funções geradoras
    - Funções geradoras utilizam a palavra reservada yield
    - Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções Generator Functions (Funções Geradoras)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
| Funções                          | Generator Functions                 |
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
| Utilizam return                  | Utilizam yield                      |
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
| REtorna uma vez                  | Podem utilizar yield multiplas vezes|
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
| Quanto executada, retorna valor  | Quando executada, retorna generator |
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""


# Exemplo Generator Funcion


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:  # vai incluir o valor_maximo
        yield contador
        contador = contador + 1


# OBS: Uma Generator funcion gera Generators

gen = conta_ate(5)

print(type(gen))
print(gen)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))  # dá erro

print(next(gen))

for num in gen:  # vai começar do 2
    print(num)

lista = list(conta_ate(5))
print(lista)

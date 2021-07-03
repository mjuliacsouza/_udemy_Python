"""
Criando sua própria versão de loop


for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Geek University')
"""

# O que acontece num for por debaixo dos panos:


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

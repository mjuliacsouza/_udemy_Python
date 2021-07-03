"""
Escrevendo um iterador customizado

# Havíamos o range():
for n in range(11):
    print(n)  # vai imprimir de 0 a 10
"""


class Contador:

    # função construtor
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 4)
print(f'menor: {con.menor}')
print(f'maior: {con.maior}')

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # dá StopOIteration pois contador está até 4 (não incluso)

for n in Contador(1, 4):
    print(n)

"""
POO - Objetos

Objetos -> São instâncias da classe. Após o mapeamento do objeto, podemos criar
quantos objetos forem necessários. São variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def lisgar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# Instancias/Objetos
lamp1 = Lampada('branca', 110, 60)
lamp2 = Lampada('azul', 220, 40)

print(f'A Lampada 1 está ligada? {lamp1.checa_lampada()}')
print(f'A Lampada 2 está ligada? {lamp2.checa_lampada()}')
print('Ligando Lâmpada 1...')
lamp1.lisgar_desligar()
print(f'A Lampada 1 está ligada? {lamp1.checa_lampada()}')
print(f'A Lampada 2 está ligada? {lamp2.checa_lampada()}')

"""
Por que testar o código?

    - Reduzir bugs
    - Testes garantem que novos recursos da aplicação não quebrem
recursos antigos
    - Garantem que bugs corrigidos anteriormente continuem corrigidos
    - Garantem que a refatoração não traga novos bugs

TDD - Test Driven Development

Com TDD é utilizado estágios de desenvolvimento:
    - Escreve os testes
    - Deseolvimento mínimo para executar teste com sucesso
    - Refatoração para realizar a funcionalidade
    - Teste passando de novo o recurso está completo
Chamados de:
    - Red
    - Green
    - Refactor
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')
felix.miar()
print(felix.nome)

import unittest

from atividades import comer, dormir, eh_engracado


class AtividadesTestes(unittest.TestCase):

    def test_comer(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comida_gostosa(self):
        """Testando o retorno com comida não saudável."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque só se vive uma vez!'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continua consado após dormir por 4 horas'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Putz, dormi muito!'
        )

    def test_eh_engracado(self):
        self.assertEqual(eh_engracado('Sergio Malandro'), False)
        # self.assertFalse(eh_engracado('Sergio Malandro'))  # não utilizar se a função não está implementada,pois retornará None que pe False


if __name__ == '__main__':
    unittest.main()

# rodar no terminal: python testes.py

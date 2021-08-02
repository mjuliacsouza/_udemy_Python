import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):

    def test_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comida_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque só se vive uma vez!'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continua consado após dormir por 4 horas'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Putz, dormi muito!'
        )


if __name__ == '__main__':
    unittest.main()

# rodar no terminal: python testes.py

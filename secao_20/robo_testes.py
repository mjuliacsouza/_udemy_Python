import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('SetUp sendo executado...')

    def test_carregar(self):
        # megaman = Robo('Mega Man', bateria=50), usa no setUp
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        # megaman = Robo('Mega Man', bateria=50), usa no setUp
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49')

    def tearDown(self):
        print('TearDown sendo executado...')


if __name__ == '__main__':
    unittest.main()

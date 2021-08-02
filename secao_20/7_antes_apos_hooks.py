"""
Unittest - Antes e após hooks

hooks -> São os testes em si, ou seja, a sua execução

Aqui estamos falando sobre fazer coisas antes e depois dos testes.

setup() -> é executado antes de cada método de teste, útil pra criar
instância de obtidos e outros dados.

tearDown() -> é executado ao final de cada método de teste. É util ao
excluir dados ou fechar conexoes de bancos de dados.
"""
import unittest

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apóso teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apóso teste
        pass

    def tearDown(self):
        # configurações do tearDown
        pass

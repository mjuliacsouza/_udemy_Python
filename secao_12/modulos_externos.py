"""
Utilizando módulos externos

Utilizamos o gerenciador de pacotes Python chamado PIP -> Python Installer Package

Installar PIP e ver o site
colorama -> Utilizado para permitir a impress~çao de textos coloridos no terminal
"""

from colorama import Fore, Back, init

init()
print(Fore.RED + 'Geek University')
print(Fore.YELLOW + 'Python')
print(Fore.BLUE + "Nicolas")
print(Back.WHITE + 'OIE')

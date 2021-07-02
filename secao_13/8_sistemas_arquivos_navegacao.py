"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operation Systems

# Fazer o import
import os

# getcwd() -> Pega o current work directory - onde vc está
# Retorna o path absoluto
print(os.getcwd())

# Para mudar o diretório podemos usar o chdir()
os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('Users/mjuli/OneDrive'))  # False

# OBS para usuário Windows:
# Cuidado ao verificar diretórios.

# Podemos identificar o sistema operacional
import sys

print(os.name)  # nt (windows)

# Podemos ver detalhes do sistema
# print(os.uname()), não funciona no windows
print(sys.platform)

# Mudando de diretório
print(os.getcwd())
res = os.path.join(os.getcwd(), 'teste')
os.chdir(res)
print(os.getcwd())
"""

import os

# Podemos listas os arquivos e diretórios
print(os.listdir())
print(len(os.listdir()))

print(list(os.scandir()))  # dá mais informações

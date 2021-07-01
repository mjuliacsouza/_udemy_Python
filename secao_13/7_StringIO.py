"""
StringIO

ATENÇÂO: Para ler ou escrever dados m arquivos do sistema operacional, o
software precisa ter permissão:
    - Leitura -> Para ler o arquivo
    - Escrita -> Para escrever o arquivo

StringIO -> Utilizado para ler e crar arquivos em memória.
"""

# Fazendo o import
from io import StringIO

mensagem = "Apenas uma string."

# Podemos criar um arquivo em memória com essa string
arquivo = StringIO(mensagem)  # abre o arquivo também
print(arquivo.closed)  # o arquivo está aberto

# Agora para ler, usamos o que já sabemos
print(arquivo.read())

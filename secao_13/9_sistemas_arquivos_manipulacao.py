"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('./teste/oi.txt'))  # True
print(os.path.exists('../secao_13'))  # True

# Criando arquivos

# Forma 1
open('./teste/TESTE.txt', 'w').close()
open('./teste/TESTE2.txt', 'a').close()

# Forma 2
# os.mknod('./teste/TESTE3.txt'), não funciona no windows

# Criando diretórios
os.mkdir('teste2')  # wtf, esse funciona

# OBS: Se não tivermos autorização para usar o diretório, teremos PermissionError
# Podemos ignorar com o parâmetro exist_ok=True

# Renomeando
os.rename('teste2', 'teste02')

# Podemos ter muitos erros

# Removendo diretórios vazios
os.rmdir('teste02')

# Removendo uma árvore de diretórios
for arquivo in os.scandir('geek'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Ao remover eles não vao pra lixeira, eles são removidos.
"""
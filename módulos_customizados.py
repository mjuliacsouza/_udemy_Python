"""
Módulos customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos criados
no curso são módulos Python prontos para serem utilizados

# Importando função especifica

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""

# Importando tudo

import funcoes_com_parametro as fcp

print(fcp.soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

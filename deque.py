"""
Módulo collections - Deque

Podemos dizer que o deque é uma lsita de alta performance.
"""

# Importa
from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos

deq.append('y')  # adiciona no final
print(deq)

deq.appendleft('k')  # add a esquerda
print(deq)

# Remover elementos
print(deq.pop())  # remove no final e retorna
print(deq)

print(deq.popleft())  # remove no começo e retorna
print(deq)

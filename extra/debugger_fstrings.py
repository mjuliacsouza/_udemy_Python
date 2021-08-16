"""
Debuggando com F-strings

# Exemplos:


def multiplicar(num1: float, num2: float) -> float:
    return num1 + num2


resultado: float = multiplicar(4.236, 6.987)

print(f'O resultado é {resultado}')

print(f'Outro resultado é {multiplicar(3.987, 3.982)}')

print(f'{(media := 8 / 2)} é a metade de {media * 2}')
print(media)
"""

geek: str = 'Geek University'

print(f'geek={geek}')

# usando f-strings, podendo debuggar o código

print(f'{geek=}')

print(f'{geek.upper()[::-1] = }')

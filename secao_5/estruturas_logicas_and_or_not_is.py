"""
Estrturas logicas: and, or, not, is

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido
Para o 'is',

"""

ativo=False
logado=False

'''
# Estrutura AND

if ativo and logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
'''

'''
# Estrutura OR 

if ativo or logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
'''

'''
# Estrutura NOT

if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem-vindo usuário")
'''

# Estrutura IS
print(ativo is True)

var = None
if not var:
    print('oi')
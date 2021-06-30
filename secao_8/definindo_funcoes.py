"""
Definindo Funções

- Funções são pequenos trechos de código que realizam taredas específicas
- Pode ou não receber entradas de dados e retornar saida de dados
- Muito úteis para executar procedimentos similares por repetidas vezes

OBS: Se vc escrever uma função que realiza várias taredas dentro dela, é bom
fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções:
    - print()
    - len()
    - max()
    - min()
    - etc

# Exemplo de utilização de funções:

cores = ['verde', 'azul', 'amarelo', 'vermelho']

# Utilizando a função integrada (Built-in) do Python: print(), para qualquer objeto
print(cores)

# Função append, apenas para o objeto listas
cores.append('roxo')

print(cores)

# Função clear(), não recebe dados de entrada
cores.clear()
"""
# ------------------------------------------------------------------------------

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco da função
    
Onde:
    - Nome da função -> sempre com letras minúsculas, e se for composto, 
    separado por udnerline('_')
    - Parâmetro de entrada -> opcionais, onde tendo mais de um, separados 
    por vigula
    - Bloco da Função -> é onde o processamento da função ocorre, pode ter
    um retorno.

OBS: Para definir uma função, utilizamos a palavra reservada 'def' e abrimos
um bloco com ':', que é utilizado em Python pra definir blocos.
"""
"""
# Definindo a primeira função

def diz_oi():
    print('oi')


OBS:
    1 - Veja que, dentro das nossas funções, podemos utilizar outras funções;
    2 - Veja que nossa função só tem uma tarefa;
    3 - Veja que não recebe nenhum parâmetro de entrada;
    4 - Veja que essa função não retorna nada


# Chamando a função para executá-la
diz_oi()
print(diz_oi())  # retorna None


ATENÇÃO:

Nunca esqueça de utilzar '()' no final ao executar uma função.
"""

# Exemplo 2:


def cantar_parabens():
    print("Parabéns pra você")
    print("Nessa data querida")
    print('...')


for i in range(4):
    cantar_parabens()  # executa 4 vezes
    print(i)


# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar
# esta função através dessa variável.

canta = cantar_parabens

canta()

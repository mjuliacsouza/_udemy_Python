"""
O que são decoradores? (Decorators)

- Decorators são funções (First Class Citizen);
- Envolvem outras funções e aprimoram seus comportamentos;
- São exemplos de HOF's
- Têm sintaxe própria, usando "@" (Syntaxe Sugar)

# Decorators como funções (Sintaxe n recomendada/ sem sugar)


def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo


def saudacao():
    print("Seja vem vinde à Geek University!")


seja_educado(saudacao)

# Estamos aprimorando a função saudação
"""

# Decorators com Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um bom dia!")
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro!")


# Testando

apresentando()

# Visualmente mais simples e facil de entender


@seja_educado_mesmo
def dormir():
    print("Quero dormir...")


dormir()

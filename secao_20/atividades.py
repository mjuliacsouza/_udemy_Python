def comer(comida, eh_saudavel):
    if eh_saudavel == True:
        final = 'quero manter a forma.'
    else:
        final = 'só se vive uma vez!'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return 'Putz, dormi muito!'
    else:
        return f'Continua consado após dormir por {num_horas} horas'


def eh_engracado(pessoa):
    lista = ['Charles Chaplin', 'Jim Carrey']
    if pessoa in lista:
        return True
    else:
        return False

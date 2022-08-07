'''101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


#considerar ano de 2018

def voto(ano):
    """

    :param val:
    :return:
    """
    '''from datetime import date
    anoat = date.today().year
    print(anoat)'''

    anoat = 2018
    id = anoat - ano
    if id < 18:
        return f'Com {id} anos: NÃO VOTA.'
    elif id >= 18:
        return f'Com {id} anos: VOTO OBRIGATÓRIO.'
    elif id > 65:
        return f'Com {id} anos: VOTO OPCIONAL.'


# Programa Principal
print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


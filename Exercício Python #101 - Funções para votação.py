'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(ano):
    from datetime import date
    anoat = date.today().year
    #return f'Ano atual: {anoat}'
    id = anoat - ano
    #return f'Idade atual: {id} anos'
    if id < 16:
        return f' \033[32mCom {id} anos: NÃO VOTA\033[m'
    elif id >= 16 and id < 18 or id > 65:
        return f'\033[34mCom {id} anos: VOTO OPCIONAL\033[m'
    else:
        return f'\033[36mCom {id} anos: VOTO OBRIGATÓRIO\033[m'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

































'''print('-' * 30)
def voto(ano):
    from datetime import date
    atual = date.today().year
    id = atual - ano
    if id < 16:
        return f'Com {id} anos: NÃO VOTA!'
    elif 16 <= id < 18 or id > 65:
        return f'Com {id} anos: VOTO OPCIONAL!'
    else:
        return f'Com {id} anos: VOTO OBRIGATÓRIO!'

#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))'''
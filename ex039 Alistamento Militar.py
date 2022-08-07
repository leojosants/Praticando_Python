'''DESAFIO 039 - Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai alistar ao serviço militar.
- Se é a hora de se alistar.
- Se ja passou do tempo do alistamento.
- Seu programa também deverá mostrar o tempo que passou ou que passou o prazo.'''

'''from datetime import date
ano = date.today().year
print(date) # comando que busca o ano configurado na maquina'''

anoatual = 2017
datanasc = int(input('Digite o ano do seu nascimento: '))
id = anoatual - datanasc
print('Quem nasceu no ano {} tem {} anos em {}'.format(datanasc, id, anoatual))
if id == 18:
    print('\033[7mVocê tem que se alistar IMEDIATAMENTE!\033[m')
elif id < 18:
    saldo = 18 - id
    print('Voce ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
elif id > 18:
    saldo = id - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))

'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos:(MIRIM) - Até 14 anos: (INFANTIL) - Até 19 anos: (JUNIOR) - Até 25 anos: (SÊNIOR) - Acima: (MASTER)'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta possui {} anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 25:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
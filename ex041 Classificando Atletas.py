'''DESAFIOV041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
 mostre sua categoria, de acordo com a idade:
 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JUNIOR
 - Até 20 anos: SÊNIOR
 - Acima: MASTER'''

'''from datetime import date
atual = date.today().year
print(atual)'''
anonasc = int(input('Qual seu ano de nascimento? '))
anoat = 2017
id = anoat - anonasc
print('Você tem {} anos.'.format(id))
if id <= 9:
    print('ATLETA MIRIM')
elif id <= 14:
    print('ATLETA INFANTIL')
elif id <= 19:
    print('ATLETA JUNIOR')
elif id <= 20:
    print('ATLETA SÊNIOR')
else:
    print('MASTER')

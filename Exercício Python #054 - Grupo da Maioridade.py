'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas já sáo maiores. Considere a maior idade com 21 anos.
'''
from datetime import date
anoat = date.today().year
totmaior = totmenor = 0
for c in range(1, 8):
    dn = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    id = anoat - dn
    #print('em {} essa pessoa possui {} anos'.format(anoat, id))
    if id > 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))

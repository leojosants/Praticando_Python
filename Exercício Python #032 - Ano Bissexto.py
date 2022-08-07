'''Faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''
from datetime import date
anoat = int(input('Qual ano quer analisar? Coloque zer para analisar o ano atual: '))
if anoat == 0:
    anoat = date.today().year
if anoat % 4 == 0 and anoat % 100 != 0 or anoat % 400 == 0:
    print('O ano {} é BISSEXTO'.format(anoat))
else:
    print('O ano {} NÃO É BISSEXTO'.format(anoat) )
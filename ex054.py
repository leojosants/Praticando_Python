'''DESAFIO 054 - crie um programa que leia o ano de nascimento de sete
 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já sao maiores.'''

#from datetime import date
#anoatual = date.today().year
#print(anoatual)
anoatual = 2017
totmaior = totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    id = anoatual - nasc
    if id >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))

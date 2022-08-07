'''DESAFIO 070 -  Crie um programa que leia o nome e o preço de varios
produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- Qual é o total gasto na compra.
- Quantos produtos custam mais de R$1.000,00.
- Qual é o nome do produto mais barato.'''

totcompra = totprodmil = 0
barato = cont = menor = 0
while True:
    nomep = str(input('Nome do produto: '))
    precop = float(input('Preço do produto: R$'))
    cont += 1
    totcompra += precop
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        #if precop > 0:
            #totcompra += precop
        if precop > 1000:
            totprodmil += 1
        if cont == 1 or precop < menor:
            menor = precop
            barato = nomep
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Qual é o total gasto na compra: R${totcompra:.2f}')
print(f'Quantos produtos custam mais de R$1000: {totprodmil}')
print(f'Qual é o nome do produto mais barato: {barato} que custa R${menor:.2f}')

'''
Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) - Qual é o total gasto na compra; B) - Quantos produtos custam mais de R$1000; C) - Qual é o nome do produto mais barato.
'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço do Produto: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto


    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto nas compras foi R${total:.2f}')
print(f'{totmil} produtos custam mais de R$1000')
print(f'{barato} é o produto mais barato custando R${menor}')
'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar: CONSIDERE US$1,00 = R$3,27'''
valor = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = valor / 3.27
print('Com R${}, voce pode comprar US${:.2f}'.format(valor, dolar))
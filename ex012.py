'''DESAFIO 012 - Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

val = float(input('Qual o valor do produto? R$ '))
print('O novo valor com desconto de 5% é R${:.2f}'.format(val-(val*5)/100))
print(f'O valor de R${val:.2f} com 5% de desconto, resulta em R${(val-(val * 5) / 100):.2f}')

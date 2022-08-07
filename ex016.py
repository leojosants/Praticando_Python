'''DESAFIO 016 - Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcção inteira. '''

'''
num = float(input('Digite um número: '))
print('Sua porção inteira é: {}'.format(int(num)))
'''

from math import trunc
nun = float(input('Digite um número: '))
print('Sua porção inteira é: ', trunc(nun))

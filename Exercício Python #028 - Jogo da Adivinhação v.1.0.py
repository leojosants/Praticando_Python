'''Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu'''
from random import randint
from time import sleep
comp = randint(0, 5)
jog = int(input('Em que numero pensei? '))
print('Processando...')
sleep(2)
if jog == comp:
    print('Eu escolhi o valor {}! PARABENS'.format(comp))
else:
    print('Eu escolhi o numero {}! VOCE PERDEU'.format(comp))
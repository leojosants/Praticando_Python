'''DESAFIO 028 - Escreva um programa que faça o computador "PENSAR" em um numero inteiro entre 0 e 5,
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu'''

from random import randint
from time import sleep
comp = randint(0, 5)
#print(comp)
num = int(input('Vou pensar em um número entre 0 e 5. Tente advinhar... '))
print('P R O C E S S A N D O  . . .')
sleep(3)
if comp == num:
    print('Jogador VENCEDOR')
else:
    print('Jogador PERDEU.\nComputador escolheu: {}'.format(comp))

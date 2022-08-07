'''Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente de sse angulo.'''
from math import sin, cos, tan, radians
ang = int(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ang))
print('O angulo de {}º tem o SENO de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {}º tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {}º tem a TANGENTE de {:.2f}'.format(ang, tangente))

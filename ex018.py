'''DESAFIO 018 - Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo'''

from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
se = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(se, co, ta))

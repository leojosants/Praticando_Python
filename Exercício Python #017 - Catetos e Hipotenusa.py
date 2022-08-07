'''Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimeito da hipotenusa.'''
from math import hypot
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa do triangulo vai medir {:.2f}'.format(hypot(catadj, catop)))
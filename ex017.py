'''DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
, calcule e mostre o comprimento da hipotenusa'''

from math import hypot
catop = float(input('Cateto Oposto: '))
catadj = float(input('Cateto Adjacente: '))
#hip = (catop ** 2 + catadj ** 2) ** (1/2)
#print(hip)
hip = hypot(catop, catadj)
print('A Hipotenusa é: {:.2f}'.format(hip))

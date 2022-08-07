'''DESAFIO 035 - Analisando Triângulo- Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas
 podem ou nao formar um triangulo'''
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento : '))
c = float(input('Terceiro segmento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Esses valorem PODEM FORMAR um triangulo.')
else:
    print('Esses valorem NÃO PODEM FORMAR um triangulo.')

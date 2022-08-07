'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não forma um triangulo'''
a = float(input('Digite o comprimento da reta A: '))
b = float(input('Digite o comprimento da reta B: '))
c = float(input('Digite o comprimento da reta C: '))
if a < b + c and b < a + c and c < a + b:
    print('Com essas medidas "SE PODE" formar um triagulo')
else:
    print('Com essas medidas "NÃO SE PODE" formar um triagulo')
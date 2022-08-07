'''Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR'''
num = int(input('Digite um numero qualquer: '))
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O numero {} é impar'.format(num))
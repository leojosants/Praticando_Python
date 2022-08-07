'''DESAFIO 023 SEPARANDO DÍGITOS DE UM NÚMERO - Faca um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.'''

num = int(input('Digite um número entre 0 e 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
milh = num // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena : {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar : {}'.format(milh))

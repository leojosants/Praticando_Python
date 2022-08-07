'''DESAFIO 033 - Faça um programa que leia tres numeros e mostre qual é o MAIOR e qual é o MENOR'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número : '))
n3 = int(input('Terceiro número: '))
'''if n1 > n2 > n3:
    print('MAIOR: {}'.format(n1))
if n2 > n1 > n3:
    print('MAIOR: {}'.format(n2))
if n3 > n2 > n1:
    print('MAIOR: {}'.format(n3))
if n1 < n2 < n3:
    print('MENOR: {}'.format(n1))
if n2 < n1 < n3:
    print('MENOR: {}'.format(n2))
if n3 < n2 < n1:
    print('MENOR: {}'.format(n3))'''
menor = n1
if n2 < n1 and n2 < n3:
    menor= n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é : {}'.format(maior))
print('o menor numero é: {}'.format(menor))

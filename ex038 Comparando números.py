'''DESAFIO 038 - Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior.
- O segundo valor é maior.
Não existe valor maior, os dois sao iguais.'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais.')

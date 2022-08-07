'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

'''def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


l = float(input('Comprimento (m): '))
c = float(input('Largura (m): '))
area(l, c)'''

def lin(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


lin('CONTROLE DE TERRENOS')
l = float(input('Largura (m): '))
c = float(input('Comprimento(m): '))
area(l, c)
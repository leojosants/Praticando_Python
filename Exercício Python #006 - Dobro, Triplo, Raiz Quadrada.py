'''Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.'''
'''n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro é {}, \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(d, t, r))'''
n = int(input('Digite um número: '))
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n, (n*3)))
print('A raiz de {} é {}'.format(n, pow(n, (1/2))))

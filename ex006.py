'''DESAFIO 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''


n = int(input('Digite um número: '))
print('O dobro de {} vale: {}'.format(n, n*2))
print('O triplo de {} é: {}'.format(n, n*3))
#print('A raiz de {} é: {:.2f}'.format(n, (n**(1/2))))
print('A raiz de {} é {}'.format(n, pow(n, (1/2))))

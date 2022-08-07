'''desafio 060 - Faça um programa que leia um numero qualquer e
mostre seu fatorial.'''

'''from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}:'.format(n, f))'''

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end =' ')
    f *= c
    c -= 1
print('{}'.format(f))

'''f = 1
n = int(input('Digite um valor para ver o fatorial: '))
for c in range(n, 0, -1):
    print(c, end=' ')
    if c > 1:
        print('x', end=' ')
    else:
        print(' =', end=' ')
    f *= c
print('{}'.format(f))'''

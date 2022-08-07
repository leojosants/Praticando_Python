'''DESAFIO 052 -  Faca um programa que leia um numero inteiro e diga
 se ele é ou nao um numero primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO')

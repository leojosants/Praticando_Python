'''
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.
'''
from time import sleep

for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)
print('Acabou')

for c in range(1, 50+1):
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.5)
print('Acabou')
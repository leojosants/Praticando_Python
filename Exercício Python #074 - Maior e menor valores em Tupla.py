'''
Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla.
'''
from random import randint
maior = menor = 0
sorteio = (randint(0, 5), randint(0, 5),
           randint(0, 5), randint(0, 5),
           randint(0, 5))
print(f'Os numeros sorteados foram {sorteio}.')
print(f'O maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')
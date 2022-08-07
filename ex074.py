'''DESAFIO ex074 - Crie um programa que vai gerar cinco numeros aleatórios e
colocar dentro de uma tupla. Depois disso, mostre a listagem de numeros
gerados e tambem indique o menor e o maior valor que estão na tupla'''

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {n}')
print(f'O menor valor sorteado foi: {min(n)}')
print(f'O maior valor sorteado foi: {max(n)}')

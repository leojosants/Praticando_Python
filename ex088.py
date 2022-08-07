'''DESAFIO 088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
 em uma lista composta.'''
'''from random import randint
soteio = [randint(1, 60), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61)]
while True:
    resp = int(input('Quantos jogos serão gerados: '))
    for c in resp(0, resp):
        print(c)
    if resp == resp:
        break
print(soteio)'''

from random import randint
from time import sleep
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
jogos = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
#print(f'Os numeros sorteados foram: {jogos}')
#print(len(jogos))
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)
print('-='*5, f' < BOA SORTE! >', '-='*5)
'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
'''
from random import randint
from time import sleep
from operator import itemgetter
print()
print('\033[7m== Valores Sorteados ==\033[m')
print()
sleep(1)
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = ()
#print(jogo)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#itemgetter coloca em ordem as chaves, adicionando e ordem reversa
#print(ranking)#ATENÇÃO IMPRIMI UMA LISTA DENTRO DE UMA TUPLA
print()
print(' \033[7m== Ranking dos jogadores ==\033[m')
print()
sleep(1)
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
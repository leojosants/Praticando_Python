'''DESAFIO 091'''

from time import sleep
from random import randint
from operator import itemgetter
sorteados = {}
sorteados['jogador1'] = randint(1, 6)
sorteados['jogador2'] = randint(1, 6)
sorteados['jogador3'] = randint(1, 6)
sorteados['jogador4'] = randint(1, 6)
ranking = ()
print('Valores soteados:')
for k, v in sorteados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-=' * 20)
ranking = sorted(sorteados.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for k, v in enumerate(ranking):
    print(f'  {k+1}º lugar: {v[0]}, com {v[1]} pontos')
    sleep(1)
print('-='*30)
'''DESAFIO 068 - faça um programa que jogue par ou impar
com o computador. O jogo so será interrompido quando o jogador perder,
mostrando o total de vitorias consecutivas que ele conquistou no final
do jogo'''

'''totjogo = totjc = 0
from random import randint
computador = randint(0, 10)
print('=-'*15)
print('Vamos jogar PAR ou ÍMPAR')
print('=-'*15)
while True:
    jogador = int(input('Digite um valor: '))
    opc = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}.', end=' ')
    totjogo = jogador + computador
    totjc = totjogo
    if totjogo % 2 == 0 and opc == 'P':
        print(f'Total de {totjogo} DEU PAR.')
    elif totjogo % 2 == 1 and opc == 'I':
        print(f'Total de {totjogo} DEU ÍMPAR.')
    if jogador != totjc:
        break'''

from random import randint
v = 0
while  True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você VENCEU!')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {v} vezes.')

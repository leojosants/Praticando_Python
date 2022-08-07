'''DESAFIO 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('JOGADOR jogou: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[34mMais... Tente novamente\033[m')
        elif jogador > computador:
            print('\033[35mMenos... Tente novamente\033[m')
print('Acertou com {} tentativas!'.format(palpites))

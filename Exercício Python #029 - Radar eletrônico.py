'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/hr, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite '''
from time import sleep
vel = int(input('Qual sua velocidade atual (Km)? '))
print('P R O C E S S A N D O . . .')
sleep(2)
if vel > 80:
    print('M .. U..  L..  T..  A..  D..  O.. \nVoce ultrapassou o limite de velocidade nesse trecho \nCalculando multa.....')
    sleep(2)
    valmult = 7 * (vel - 80)
    print('Valor da multa será de R${:.2f}'.format(valmult))
else:
    print('PARABENS, VC ESTÁ DENTRO DO LIMITE DE VELOCIDADE PARA ESSE TRECHO \nTENHA UMA BOA VIAGEM!')
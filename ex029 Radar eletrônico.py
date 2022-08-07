''' DESAFIO 029 Radar eletrônico - Escreva um programa que leia a velocidade de um carro.
- Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
- A multa vai custar R$7,00 por cada Km acima do limite'''

veloc = float(input('Qual a velocidade do carro? Km/h '))
if veloc > 80:
    print('O limite de velocidade neste trajeto é de 80 Km/h!')
    print('Voce estava com a velocidade de: {} Km/h e será multado!'.format(veloc))
    mult = 7 * (veloc - 80)
    print('MULTA: R${:.2f}'.format(mult))
print('Siga em frente, Boa Viagem !!!')

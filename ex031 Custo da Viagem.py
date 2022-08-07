'''DESAFIO 031 Custo da Viagem - Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preco da passagem, cobrando R$0,50 por Km para viagens de até 200 Km e R$0.45 para viagens mais longas'''

distancia = float(input('Digite qual a distância da viagem: '))
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print('Valor da passagem: R${:.2f}'.format(preco))

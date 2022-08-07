'''Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preco da passagem. Cobrando R$0,50 por Km para viagens ate 200km e R$0,45 para viagens mais longas'''
dist = float(input('Qual a distancia a ser percorrida (Km)? '))
if dist <= 200:
    viagcurta = dist * 0.50
    print(' valor da passagem sairá a R${:.2f}'.format(viagcurta))
else:
    viaglonga = dist * 0.45
    print('O valor da passagem sairá a R${:.2f}'.format(viaglonga))
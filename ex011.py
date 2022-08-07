'''DESAFIO 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²'''

larg = float(input('Largura: '))
alt = float(input('Altura: '))
area = larg * alt
print('A área dessa superfície é: {:.2f}m².'.format(area))
print('Para pintar essa superfície, será necessário {:.1f} L de tinta.'.format(area/2))
print(f'A área de uma superfície com as seguintes dimenções:\n'
      f'- Lagura: {larg}\n'
      f'- Altura: {alt}\n'
      f'- Área: {larg} x {alt} = {larg * alt:.2f}m²')
print(f'Para pintar essa área de {larg * alt:.2f}m², será necessário {(larg * alt) / 2:.2f} litros de tinta.')
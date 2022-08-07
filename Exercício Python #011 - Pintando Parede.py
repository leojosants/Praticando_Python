'''Faca um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2'''
larg = float(input('Largura da parede (m)? '))
alt = float(input('Altura da parede (m)? '))
área = larg * alt
tottinta = área / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, área))
print('Para pintar essa parede, será necessário {}l de tinta'. format(tottinta))
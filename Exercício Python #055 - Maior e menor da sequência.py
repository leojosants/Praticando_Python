'''
Faca um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.
'''
maiorp = menorp = 0
for c in range(1, 6):
    peso = float(input('Qual peso da {}ª pessoa?(Kg): '.format(c)))
    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O maior peso digitado foi {}Kg'.format(maiorp))
print('O menor peso digitado foi {}Kg'.format(menorp))
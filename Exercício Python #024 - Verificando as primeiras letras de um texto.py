'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"'''
cid = str(input('Em que cidade voce nasceu? ')).strip()
print('Essa cidade começa com o nome "SANTO"? {}'.format(cid[:5].upper() == 'SANTO'))

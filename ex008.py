'''DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros'''

'''med = float(input('Digite um valor em metros: '))
print('O valor digitado vale {} km'.format(med / 1000))
print('O valor digitado vale {} hm '.format(med / 100))
print('O valor digitado vale {} dam'.format(med / 10))
print('O valor digitado vale {} dm'.format(med * 10))
print('O valor digitado vale {} em cem'.format(med * 100))
print('O valor digitado vale {} em milimetros'.format(med * 1000))'''

med = float(input('Digite um valor em metros: '))
#km = med / 1000
print('O valor {} metros convertido em KM - (Quilômetro) é: {}'.format(med, med / 1000))
#print(f'O valor {med} metros convertido em KM é: {km}')
#print('O valor {} metros convertido em KM é: {}.'.format(med, km))
print(f'O valor {med} metros convertido em HM - (Hectômetro) é: {med / 100}')
print(f'O valor {med} metros convertido em DAM - (Decâmetro) é: {med / 10}')
print(f'O valor {med} metros convertido em DM - (Decímetro) é: {med * 10}')
print(f'O valor {med} metros convertido em CM - (Centímetro) é: {med * 100}')
print(f'O valor {med} metros convertido em MM - (Milímetros) é: {med * 1000}')

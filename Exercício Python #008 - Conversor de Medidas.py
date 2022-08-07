'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
n = int(input('Digite uma distancia (m): '))
km = n / 1000
hm = n / 100
dam = n / 10
dec = n * 10
cent = n * 100
mil = n * 1000
print('A medida de {}m corresponde a: '.format(n))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}m'.format(km, hm, dam, dec, cent, mil))

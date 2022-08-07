'''Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
FORMULA DE CONVERSÃO: F = ((9 * C) / 5) + 32'''
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('A temperatura {}ºC corresponde a {}ºF'.format(c, f))
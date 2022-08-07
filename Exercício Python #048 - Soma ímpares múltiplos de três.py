'''
Faca um programa que calcule a soma de todos o numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500
'''
s = cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma entre os {} valores digitados é {}.'.format(cont, s))
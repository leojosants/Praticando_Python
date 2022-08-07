'''DESAFIO 048 - Faça um programa que calcule a soma entre todos os
numeros impares que são multiplos de tres e que se encontram no intervalo de 1 ate 500.'''

s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
        #print(c)
print('Soma dos {} numeros solicitados é {}.'.format(cont, s))

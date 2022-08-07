'''
Refaca o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
'''
#DESAFIO 051
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimotermo = primeiro + (10 - 1) * razão#para saber o deci o termo, formula: primeiro termo adicionado com o resultado da subtração do decimo termo menos um vezes a razão
for c in range(primeiro, decimotermo + razão, razão):
    print(c, end=' -> ')
print('Fim')


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')
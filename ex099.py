'''099: Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.'''

from time import sleep
def maior(*num):
    cont  = 0
    print('-='*20)
    print('Analisando os valores informados...')
    for valor in (num):
        print(f'{valor}', end='- ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} valores.')
    print(f'O maior valor foi {maior}')
    #print(f'O maior valor foi {max(num)}') função direta (max), que busca o maior numero

# Programa Principal
maior(1, 6, 4, 2, 5)
maior(3, 7, 4)
maior(0,6)
maior(6)
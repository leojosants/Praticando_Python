'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(* num):
    cont = maior = 0
    print('-x-' * 20)
    print(f'Analisando os valores repassados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor digitado foi {maior}')

maior(3, 5, 2, 1,-4)
maior(-3, 3, -0, 5)
maior(2, 9, 34, 5, 0)
maior()
maior(0)
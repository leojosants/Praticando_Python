''' 098: Faça um programa que tenha uma função chamada contador(), que receba três
 parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
 através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

'''from time import sleep

def contadorcres(*num):
    print('-='*15)
    print('Contagem de 1 a 10 de 1 em 1: ')
    for v in range(*num):
        print(v, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*15)

def contadordecresc(*num):
    print('Contagem de 10 a 0 de 2 em 2: ')
    for v in range(*num):
        print(v, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*15)

def contagempers(a, b, c):
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for v in range(inicio, fim, passo):
        print(v, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*15)

# Programa Principal
contadorcres(1, 11, 1)
contadordecresc(10, 0, -2)
contagempers('inicio', 'fim', 'passo')'''


from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM !')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM !')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
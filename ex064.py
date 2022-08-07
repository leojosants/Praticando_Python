'''DESAFIO 064 - Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar 999, que é a consição de parada.
 No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
Desconsiderando o flag'''

n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        print('Foram digitados {} número(s) e a soma de todos é {}.'.format(cont,soma ))

'''n = cont = soma = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor [999 para parar]: '))
print('Foram digitados {} numeros e a soma de todos é: {}'.format(cont, soma))'''

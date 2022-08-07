'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderar o flag)
'''
n = cont = soma = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))
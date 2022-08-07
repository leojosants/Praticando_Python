'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderar) o flag
'''
cont = s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} valores digitados é {s}')
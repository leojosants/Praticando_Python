'''DESAFIO 066 - Crie um programa que leia varios numeros inteiros
pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,
que é a condição de parada. No final, mostre quantos numeros foram digitados
e qual foi a soma entre eles. (desconsiderar o flag)'''

s = c = 0
while True:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos \033[35m{c}\033[m valores foi \033[34m{s}\033[m.')

'''
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteudo das tres listas geradas.
'''
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista gerada foi: {lista}.')
print(f'A lista gerada com numeros pares foi: {par}')
print(f'A lista gerada com números ímpares foi: {impar}')
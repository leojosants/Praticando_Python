'''
Crie um programa que vai ler vaios numeros e colocar em uma lista. Depois disso, mostre: A) - Quantos numeros foram digitados; B)- A lista de valores ordenada de forma decrescente; C) - Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-x-' * 20)
print(f'Lista = {lista}')
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Os valores ordenados de forma decrescente = {lista}')
if 5 in lista:
    print(f'O valor 5 \033[4;37mFOI digitado\033[m.')
else:
    print('O valor 5 \033[4mNÃO FOI digitado\033[m.')

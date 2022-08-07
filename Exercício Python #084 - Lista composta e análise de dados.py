'''
Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre: A) - Quantas pessoas foram cadastradas; B) - Uma listagem com as pessoas mais pesadas; C) - Uma listagem com as pessoas mais leves.
'''
lista = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(Kg): ')))
    if len(lista) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    lista.append(dados[:])
    dados.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
#print(f'Lista = {lista}')
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
print()
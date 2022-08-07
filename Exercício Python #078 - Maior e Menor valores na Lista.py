'''
Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior valor e o menor valor valor digitado e as suas respectivas posições na lista
'''
listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posião {c}: ')))
    if c == 0:#quando não sabemos qual é o menor nem o maior quando ainda nao foi digitado nenhum valor
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O MAIOR valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O MENOR valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
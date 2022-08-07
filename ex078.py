'''DESAFIO 078 - Faça um programa que leia 5 valores numericos e guarde-os
 em uma lista. No final, mostre qual foi o maior e o menor valor digitados
 e suas respectivas posições na lista.'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
print('-='*30)
print(f'Você digitou os valores: {valores}')

for c, v in enumerate(valores):
    if max(valores) in valores:
        print(f'O maior valor digitado foi {max(valores)} nas posições {c}')
    elif min(valores) in valores:
        print(f'O menor valor digitado foi {min(valores)} nas posições {c}')
print(max(valores))
print(min(valores))'''

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
            if valores[c] < menor:
                menor = valores[c]
print('-='*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
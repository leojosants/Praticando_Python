'''
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
'''
lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)
print(lista)
print(f'Os valores pares digitados foram {sorted(lista[0])}.')
print(f'Os valores impares digitados foram {sorted(lista[1])}.')
'''DESAFIO 075 - Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares'''

'''n1 = (int(input('Digite um valor: ')))
n2 = (int(input('Digite outro valor: ')))
n3 = (int(input('Digite mais um valor: ')))
n4 = (int(input('Digite o último valor: ')))'''
num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
#9 3 2 9
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição e no indice {num.index(3)}.')
else:
    print('O numero 3 não foi encontrado entre os valores digitados.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
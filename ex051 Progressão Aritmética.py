'''DESAFIO 051 - Desenvolva um programa que leia o primeiro termo
e a razao de uma PA. no final, mostre os 10 primeiros termos
dessa progressão.'''

primeiroT = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiroT + (10 - 1) * razao
for c in range(primeiroT, decimo + razao, razao):
    print(c, end=' ->')
print('Acabou')

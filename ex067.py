'''DESAFIO 067 - Faça um programa que mostre a tabuada de varios numeros, um de cada
vez, para cada valor digitado pelo usuario. O programa será interrompido quando
o numero solicitado for negativo'''

'''while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    for c in range(0, 11):
        print(f'{n} x {c} = {c * n}')
    if n < 0:
        break
print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO.... Volte sempre!')'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

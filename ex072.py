'''DESAFIO 072 - Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero ate vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco','Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze','Dezesseis', 'Dezesete', 'Dezoito',
            'Dezenove', 'Vinte')
while True:
    resp = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= resp <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero: {contagem[resp]}')
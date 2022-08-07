'''
Crie um programa que tenha uma tupla totalmente preencida com uma contagem por extenso, de zero ate vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
numerais = ('zero', 'um', 'dois', 'trez', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
    resp = ' '
print(f'Voce digitou o número {numerais[num]}.')
'''DESAFIO 037 - Escreva um programa que leia um numero inteiro e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

numero = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] - Converter para Binária
[ 2 ] - Converter para Octal
[ 3 ] - Converter para Hexadecimal''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('A conversão do numero {} para BINARIA é: {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('A conversão do numero {} para OCTAL é : {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('A conversao do numero {} para HEXADECIMAL é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha incorreta. Tente novamente')

'''Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1= Para Binário; 2 = Para Octal; 3 = Para Hexadecimal'''
num = int(input('Escreva um número: '))
print('''1 = BINÁRIO 
2 = OCTAL
3 = HEXADECIMAL''')
opc = str(input('Qual base gostaria de convertê-lo? '))
if opc == '1':
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == '2':
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == '3':
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, Tente novamente')
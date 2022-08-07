'''DESAFIO 022 ANALISADOR DE TEXTOS - crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas.
- O nome com todas as letras minusculas.
- Quantas letras ao todu sem considerar os espaços.
- Quantas letras tem o primeiro nome
'''

nome = str(input('Qual seu nome completo: ')).strip() # strip ja elimina os espaços das extremidades
print(nome)
print('Nome em maiuscula: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
print('Meu nome completo possui: {} letras'.format(len(nome) - nome.count(' '))) #count verifica quantos espaços tem entre as palavras
dividido = nome.split()
print('Meu primeiro nome tem: {} letras'.format(len(dividido[0][0:])))

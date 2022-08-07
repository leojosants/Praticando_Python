''' DESAFIO 025 - Procurando uma string dentro de outra - Crie um programa que leia o nome de uma pessoa e diga se
ela tem "SILVA" no nome'''

nome1 = str(input('Digite seu nome completo: ')).strip().upper()
print(nome1)
print('Seu nome possui a palavra "SILVA"? {}'.format("SILVA" in nome1))

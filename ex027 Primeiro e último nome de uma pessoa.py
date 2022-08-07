''' DESAFIO 027 - Primeiro e último nome de uma pessoa - Faça um programa que leia o nome de uma pessoa, mostrando
em seguidao primeuro e o ultimo nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Muito prazer em te conhecer!')
div = nome.split()
#print(div)
print('Seu primeiro nome é {}.'.format(div[0]))
print('Seu ultimo nome é: {}.'.format(div[len(div)-1]))

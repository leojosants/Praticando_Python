'''Crie um programa que leia o nome completo de uma pessoa e mostra:
- O nome com todas as letras maiusculas; - O nome com todas as letras minusculas; - Quantas letras ao todu sem considerar espaços; - Qunats letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'. format(len(nome)-nome.count(' ')))#menos nome.cout, conta e elimina os espaços entre as palavras
dividindo = nome.split()
print(dividindo)
print('Seu primeiro nome é {} e tem {} letras'.format(dividindo[0], len(dividindo[0])))
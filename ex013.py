'''DESAFIO 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

sal = float(input('Qual o salário do funcionário? R$ '))
print('Seu novo salário acrecido de 15% é: R$ {:.2f}'.format(sal + (sal * 15) / 100))
print(f'O salário de R${sal:.2f} com acréscimo de 15%, resulta em R${sal + (sal * 15) / 100:.2f}')
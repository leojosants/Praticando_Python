'''Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento'''
sal = float(input('Qual seu salário atual? R$'))
novosal = sal + (sal * 15) / 100
print('Seu novo saláro com 15% de aumento será de R${:.2f}'.format(novosal))
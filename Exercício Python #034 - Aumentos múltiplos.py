'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1250,oo, calcule um aumento de 10%. Para os inferiores ou iguais,  aumento é de 15%.'''
sal = float(input('Digite seu salário: R$'))
if sal > 1250.00:
    nsal = sal + ((sal * 10) / 100)
    print('Seu novo salário com o aumento de 10% será R${:.2f}'.format(nsal))
if sal <= 1250.00:
    nsal = sal + ((sal * 15) / 100)
    print('Seu novo salário com o aumento de 15% será R${:.2f}'.format(nsal))
'''DESAFIO 034 - Aumentos múltiplos - Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.
- Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
- Para os inferiores ou iguais, o aumento é de 15%'''

sal = float(input('Qual o salario? R$ '))
if sal <= 1250:
    nosal = sal + (sal * 15 / 100)
    print('O novo salário acrescido de 15% é: R${:.2f}'.format(nosal))
else:
    novsal = sal + (sal * 10 / 100)
    print('O novo salário acrescido de 10% é: R${:.2f}'.format(novsal))

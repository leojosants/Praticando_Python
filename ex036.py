'''DESAFIO 036 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.'''

print('*-' * 5, 'E M P R É S T I O   B A N C Á R I O', '*-' * 5)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos quer pagar? '))
prestacao = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, anos, prestacao))
minimo = (salario * 30) / 100
if prestacao <= minimo:
    print('COMPRA ACEITA')
else:
    print('COMPRA NEGADA')

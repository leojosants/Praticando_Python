'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado
'''

valcasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do cliente? R$'))
temppag = int(input('Em quantos anos quer pagar o imóvel? '))
parcelas = temppag * 12
valmensal = valcasa / parcelas
naoexc = (sal * 30) / 100
#print(naoexc)
if valmensal < naoexc:
    print('EMPRESTIMO APROVADO... PARABENS...')
    print('{} anos equivale a {} parcelas de R${:.2f}'.format(temppag, parcelas, valmensal))
else:
   print('APROVAÇÃO NEGADA... Valor da prestação excede 30% do salário')
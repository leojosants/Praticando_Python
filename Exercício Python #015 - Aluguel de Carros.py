'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
dias = int(input('Quantos dias alugados? '))
totdia = 60 * dias
#print('O valor a ser pago pelos dias alugados é R${}'.format(totdia))
km = int(input('Quantos Km rodados? '))
totkm = 0.15 * km
#print('O valor a ser pago pela quilometragem rodada é R${:.2f}'.format(totkm))
print('O total a pagar é de R${:.2f}'.format(totdia+totkm))
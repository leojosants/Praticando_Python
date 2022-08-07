'''DESAFIO 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado'''

perc = float(input('Digite a quantidade de Km percorrido: '))
diasalu = int(input('Digite quantos dias o carro ficou alugado: '))
valpdia = (60 * diasalu)
#print('Valor total a pagar por dia é : R${:.2f}'.format(valpdia))
kmperc = (0.15 * perc)
#print('Valor total a pagar por Km rodado é: R${:.2f}'.format(kmperc))
print('Total a pagar ao final foi: R${:.2f}'.format(valpdia + kmperc))

'''DESAFIO 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até duas vezes no cartão: preço normal
- 3 vezes ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS GUANABARA '))
valprodutos = float(input('Qual o valor do produto: R$'))
opcoespag = input('''[ 1 ] - À vista dinheiro/cheque: 10% de desconto
[ 2 ] - À vista no cartão: 5% de desconto
[ 3 ] - Em até duas vezes no cartão: preço normal
[ 4 ] - 3 vezes ou mais no cartão: 20% de juros
Escolha uma opção para pagamento: ''')
#print('A opção de pagamento foi: {}'.format(opcoespag))
if opcoespag =='1':
    desconto10 = valprodutos - (valprodutos * (10 / 100))
    print('O valor a pagar com 10% de desconto é: R${:.2f}'.format(desconto10))
elif opcoespag == '2':
    avistacarddesc5 = valprodutos - (valprodutos * 5 / 100)
    print('O valor a pagar com 5% de desconto é: R${:.2f}'.format(avistacarddesc5))
elif opcoespag == '3':
    print('Valor nomal: R${:.2f}'.format(valprodutos))
elif opcoespag == '4':
    parcelas = int(input('Quantas parcelas? '))
    valjuros = valprodutos + (valprodutos * (20 / 100))
    print('o valor a pagar com 20% de juros é: {:.2f}'.format(valjuros))
    valorparc = valjuros / parcelas
    print('O valor de cada parcela será: R${:.2f}'.format(valorparc))
else:
    print('\033[3:30mOpção incorreta. Tente novamente')

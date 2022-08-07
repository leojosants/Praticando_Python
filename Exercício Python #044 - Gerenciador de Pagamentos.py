'''Elabore um programa que calcule o valor a ser pago por um produto, considere o seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em ate 2x no cartão: preço normal
- 3x ou mais no cartao: 20% de juros'''
preçop = float(input('Qual o valor das compras? R$'))
print('''OPÇÕES DE PAGAMENTO
[1] - A vista dinheiro / cartão: 10% de DESCONTO
[2] - A vista no cartão: 5% de DESCONTO
[3] - Em até 2x no cartão: PREÇO NORMAL
[4] - 3x ou mais no cartão: 20% de JUROS''')
opc = int(input('Escolha a opção para pagamento: '))
if opc == 1:
    total = preçop - ((preçop * 10) / 100)
elif opc == 2:
    total = preçop - ((preçop * 5) / 100)
elif opc == 3:
    total = preçop
    parc = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}.'.format(parc))
elif opc == 4:
    total = preçop + (preçop * 20) / 100
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc, parcela))
else:
    total = preçop
    print('\033[7mOPÇÃO INVÁLIDA.TENTE NOVAMENTE\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preçop, total))
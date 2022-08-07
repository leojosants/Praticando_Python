'''Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto'''
preco = float(input('Digite o valor do produto: R$'))
print('Esse produto com 5% de desconto, sairá a R${:.2f}'.format(preco - (preco * 5) /100))

'''DESAFIO 010 - crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.'''

valor = float(input('Qual valor você tem na carteira? R$ '))
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(valor, valor / 3.27))
conv = valor / 3.27
print(f'Com R${valor:.2f}, você pode comprar US${conv:.2f}')
print(f'Com R${valor:.2f}, você pode comprar US${valor / 3.27:.2f}')

'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''

from ex108 import  moeda# OU import moeda

p = float(input('Digite o preço: R$'))

print(f'Aumentando 10% no valor {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 10))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'Aumentando 10% no valor {p} temos {moeda.aumentar(p, 10)} ')

print(f'Diminuindo 10% no vallor {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 10))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO  # print(f'Diminuindo 10% no valor {p} temos {moeda.diminuir(p, 10)}')

print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'O dobro de {p} é {moeda.dobro(p)}')

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'A metade de {p} é {moeda.metade(p)}')

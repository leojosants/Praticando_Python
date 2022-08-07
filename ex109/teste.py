'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex109 import moeda # import moeda

p = float(input('Digite o preço: R$'))

print(f'Aumentando 10% no valor {moeda.moeda(p)} temos {moeda.aumentar(p, 10, True)}')# print(f'Aumentando 10% no valor {moeda.moeda(p)} temos {moeda.aumentar(p, 10)}') # print(f'Aumentando 10% no valor {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 10))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'Aumentando 10% no valor {p} temos {moeda.aumentar(p, 10)} ')

print(f'Diminuindo 10% no valor {moeda.moeda(p)} temos {moeda.diminuir(p, 10, True)}') # print(f'Diminuindo 10% no valor {moeda.moeda(p)} temos {moeda.diminuir(p, 10)}') # print(f'Diminuindo 10% no valor {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 10))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO  # print(f'Diminuindo 10% no valor {p} temos {moeda.diminuir(p, 10)}')

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}') # print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}') # print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'O dobro de {p} é {moeda.dobro(p)}')

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}') # print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}') # print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}') # Contem MOEDA MODULO, MOEDA FUNÇÃO, MOEDA PARAMETRO # print(f'A metade de {p} é {moeda.metade(p)}')

#help(moeda)
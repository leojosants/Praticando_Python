'''107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex107 import moeda # OU import moeda

p = float(input('Digite o preço: R$'))

print(f'Aumentando 10% no valor {p} temos {moeda.aumentar(p, 10)} ')

print(f'Diminuindo 10% no valor {p} temos {moeda.diminuir(p, 10)}')

print(f'O dobro de {p} é {moeda.dobro(p)}')

print(f'A metade de {p} é {moeda.metade(p)}')
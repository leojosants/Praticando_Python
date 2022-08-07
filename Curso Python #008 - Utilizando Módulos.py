'''IMPORTAÇÃO DE BIBLIOTECAS

Há a possibilidade de importar toda a biblioteca, importar alguns módulos ou somente importar um módulo específico pra utilização'''

'''
import biblioteca - importara todos os múdulos da biblioteca
from biblioteca import módulo  - importe somente um módulo específico

math = biblioteca com funcionalidades de matemáticas
    - ceil ( arredonda o valor pra cima)
    - floor (arredonda o valor para baixo)
    - trunc (elimina da virgula pra a frente se arredondar nada)
    - pow (potencia)
    - sqrt (raiz quadrada)
    - factorial (calculo de fatorial)
'''
'''import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))'''

'''from math import sqrt, ceil, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))'''

'''import random
num = random.random()#randomiza numero entre 0 e 1
print('O numero sorteado entre 0 e 1 foi: {}'.format(num))
num = random.randint(1, 10)#randomiza numeros inteiros entre 1 e 10
print('O numero sorteado entre 1 e 10 foi: {}'.format(num))'''

'''from random import random, randint
num = random()#randomiza numero entre 0 e 1
print('O numero sorteado entre 0 e 1 foi: {}'.format(num))
num = randint(1, 10)#randomiza numeros inteiros entre 1 e 10
print('O numero sorteado entre 1 e 10 foi: {}'.format(num))'''

import emoji
print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))

''' UTILIZANDO MODULOS'''

'''
Biblioteca math

- ceil: Arredonda para cima.
- floor: Arredonda para baixo.
- trunc: Elimina da vírgula pra frente.
- pow: Calcula a potência de um númeero.
- sqrt: Calcula a raiz quadrada de um número.
- factorial: Calcula o fatorial de um número.
- COMANDO - import math: Importa toda biblioteca
- COMANDO - from math import sqrt: Importa somente a função "sqrt" da biblioteca math
'''

''' 
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A Raiz quadrada de {} é: {:.2f}'.format(num, math.floor(raiz)))
fact = math.factorial(num)
print('O !{} é: {:.2f}'.format(num, fact))
'''

'''
from math import sqrt, factorial
num = int(input('Digite um valor: '))
raiz = sqrt(num)
print('A raiz de {} é : {}'.format(num, raiz))
fact = factorial(num)
print(('O !{} é: {}'.format(num, fact)
'''

'''
import random
num = random.random() # Gera numeros aleatórios flutuantes entre o e 1
print(num)
num2 = random.randint(1, 10) # Gera npumeros aleatórios entre 1 e 10
print(num2)
'''

'''
import emoji
print(emoji.emojize("Olá, Mundo! :sunglasses:", use_aliases=True))
'''
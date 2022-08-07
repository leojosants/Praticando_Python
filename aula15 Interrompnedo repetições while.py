'''INTERROMPENDO REPETIÇÕES WHILE'''

'''Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos 
precisamos interromper um laço no meio do caminho. Além disso, vamos aprender como trabalhar com as novas fstrings do Python.'''

'''while True:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega'''

'''s = n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format(s))'''

# FSTRINGS atualizado no Python 3.6+
'''s = n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')''' #uso da Fstring

'''nome = 'José'
idade = 38
salario = 980.40
print(f'O {nome}, tem {idade} anos.') #uso da Fstring
print('O {}, tem {} anos.'.format(nome, idade))
print(f'O {nome}, tem {idade} anos e ganha R${salario:.2f}')
print('O {}, tem {} anos e ganha R${:.2f}'.format(nome, idade, salario))'''
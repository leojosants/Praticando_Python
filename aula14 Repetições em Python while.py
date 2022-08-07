'''Repetições em Python (while)'''

'''Laços de repetição parte 2'''

'''
enquanto não "chegar na" maça:
    passo
pega
'''

'''
while not maça:
    passo
pega
'''

'''
enquanto nao maça:
    se chao
        passo
    se buraco
        pula
    se moeda
        pega
pega    
'''

'''
while not maça:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
    pega
'''

'''for c in range(1, 10):
    print(c, end=' ->>')
print('FIM')'''

#COMPARANDO A ESTRUTURA FOR COM A ESTRUTURA WHILE

'''c = 1
while c < 10:
    print(c, end=' ->')
    c += 1
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')'''

'''r = 'S'
while r =='S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer  continuar [S/N]? ')).upper()
print('FIM')'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números PARES e {} números IMPARES.'.format(par, impar))'''
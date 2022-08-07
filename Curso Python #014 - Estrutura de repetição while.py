'''
LAÇOS DE REPETIÇÃO PART II

ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

enquanto NÃO chegar na maçã             while not maça
    passo                                   passo
pega                                    pega

REPRESENTANDO EM PORTUGOL

enquanto não maçã           while not maçã
    se chão                     if chão:
        passo                       passo
    se buraco                   if buraco:
        pula                        pula
    se moeda                    if moeda:
        pega                        pega
pega                        pega
'''

'''for c in range(1, 10):
    print(c, end='-')
print('Fim')'''

'''c = 1
while c < 10:
    print(c, end='-')
    c += 1
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
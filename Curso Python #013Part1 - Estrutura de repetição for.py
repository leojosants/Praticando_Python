'''
LACOS, REPETIÇÕES OU ITERAÇÕES
'''
'''

  ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE

laco c no intervalo(1,10)       for c in range(1,10)
    passo                           passo
pega                            pega

-------------------------------------------------------------------

laco c no intervalo(0,3)        for c in range(0,3)
    passo                           passo
    pula                            pula
passo                           passo
pega                            pega

-------------------------------------------------------------------

laco c no intervalo(0,3)        for c in range(0,3)
    se                              if:
        pega                            pega
    passo                           passo
    pula                            pula 
passo                           passo
pega                            pega
'''

'''for c in range(0, 6):
    print('oi')
print('FIM')'''

'''for c in range(0, 6):
    print(c)
print('FIM')'''

'''for c in range(6, 0, -1):
    print(c)
print('FIM')'''

'''for c in range(0, 10, 2):
    print(c)
print('FIM')'''

'''n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('FIM')'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

'''s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos {} valores digitados foi {}'.format(c+1, s))'''
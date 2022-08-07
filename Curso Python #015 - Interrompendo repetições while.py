'''
    Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python,já que em alguns casos precisamos interromper um laço no meio do caminho. Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

LAÇOS DE REPETIÇÃO PART III

enquanto Verdadeiro             while True: (looping infinito)
    se chão                         if chão
        passo                           passo
    se buraco                       if buraco
        pula                            pula
    se moeda                        if moeda
        pega                            pega
    se trofeu                       if trofeu
        pula                            pula
        intenrrompa                     break (interrompe o laço infinito)
pega                            pega

'''

n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados vale {s}')
#print('A soma dos {} valores digitados vale {}'.format(c, s))
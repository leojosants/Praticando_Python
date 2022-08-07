'''
adição (+)      subtração (-)       multiplicação (*)       divisão (/)
potencia (**)   Div int (//)        resto da divisão ou módulo (%)

Ordem de Precedencia:
1 - ()      2 - **      3 - *, /, //, %     4 - +, -
'''

'''a = 5 + 3 * 2
print(a)

b = 3 * 5 + 4 ** 2
print(b)

c = 3 * (5 + 4) ** 2
print(c)

print(pow(4, 3))# 4 ao cubo'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
exp = n1 ** n2
print('A soma vale {}'.format(s))
print('A subtração vale {}'.format(sub))
print('A multiplicação vale {}'.format(mult))
print('A divisão vale {:.3f}'.format(div))
print('A divisão inteira vale {}'.format(divint))
print('A potencia vale {}'.format(exp))
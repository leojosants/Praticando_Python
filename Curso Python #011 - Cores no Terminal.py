'''ANSI escape sequence
Representando cores em Python: \033["AQUI ENTRA O CODIGO DA COR ponto e virgula"m
OBS: No local de preenchimento do código, pode ser em branco, um, dois ou tres codigos.
EX.: \033[style;text;backm - \033[0;33;44m
Códigos:
STYLE = Fonte: negrito, sublinhado
        0 None/Nenhum
        1 Bold/Negrito
        4 Underline/Sublinhado
        7 Negative/inverte fundo com letra.
TEXT = Cor da fonte
        30 Branco
        31 Vermelho
        32 Verde
        33 Amarelo
        34 Azul
        35 Magenta
        36 Ciano
        37 Cinza
BACK = Cor do fundo
        40 Branco
        41 Vermelho
        42 Verde
        43 Amarelo
        44 Azul
        45 Magenta
        46 Ciano
        47 Cinza
'''

print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!')
print('\033[31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('=*'*10)
a = 2
b = 9
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('=*'*10)
nome = 'Leonardo'
print('Olá! Muito prazer em te conhecer, {}!!!'.format(nome))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('=*'*10)
nome = 'Leonardo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
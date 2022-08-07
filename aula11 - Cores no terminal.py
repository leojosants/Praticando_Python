'''Aula 11 - Cores no terminal'''

#\033[style;text;back m

'''
 * Códigos para STYLE:
0 = Significa sem formatação
1 = Negrita o texto
4 = Sublinha o texto
7 = Invertes as cores entre letra e fundo

 * Códigos para TEXT: (cor do texto ou fonte)
30 = branco
31 = vermelho
32 = verde
33 = amarela
34 = azul
35 = magenta
36 = ciano
37 = cinza

 * códigos para BACK (cor de fundo):
 40 = branco
 41 = vermeho
 42 = verde 
 43 = amarelo
 44 = azul
 45 = magenta
 46 = ciano
 47 = cinza
'''
'''print('\033[1;31;43mOlá,  Mundo!')
print('\33[1;31;43mOlá, Mundo!\033[m') #\033[m no final da string, pede pra formatação de cores ser interrompida mo final da string
print('\33[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')'''

'''a = 3
b = 5
print('Os valores são \033[7;32m{}\033[m e \033[7;32m{}\033[m !!!'.format(a, b))'''

nome = 'Leonardo'
print('É um prazer te conhecer, {} {} {} !'.format('\033[4;34m', nome, '\033[m'))

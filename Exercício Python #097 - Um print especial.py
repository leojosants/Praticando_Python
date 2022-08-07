'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''

'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)#adequa a mensagem entre o comprimento da variavel
    print(f'  {msg}')
    print('~' * tam)


escreva('Olá, Mundo!')
escreva('Teste')
escreva('Oi')
escreva('.')'''

def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
escreva('Olá, Mundo')
escreva('Olá')
escreva('oi')
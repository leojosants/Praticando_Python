'''097: Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída: ~~~~~~~~~
       Olá, Mundo!
Saida: ~~~~~~~~~ '''

def escreva(txt):
    #print(len(txt))
    tam = len(txt) + 4 # recebe o aumento da quantidade de caracteres
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)

#Programa Principal
escreva('Olá, Mundo!')
escreva('OI')
escreva('Curso de Python no YouTube')
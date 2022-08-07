'''DESAFIO 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, so que agora utilizando um laço for.'''

num = int(input('Quer ver a tabuada de qual numero? '))
for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, (num * c)))

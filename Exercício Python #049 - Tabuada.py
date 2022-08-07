'''
Refaca o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.
'''
num = int(input('De qual numero deseja ver a tabuada? '))
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(num, c, num * c))
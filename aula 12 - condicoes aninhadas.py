'''ESTRUTURAS DE CONTROLE'''
'''CONDIÇÕES ANINHADAS'''
'''
SE carro.esquerda ();               ---         if carro.esquerda():
    BLOCO 1                         ---             BLOCO 1
SENAO SE carro.direita():           ---         elif carro.direita():
    BLOCO 2                         ---             BLOCO 2
SENAO:                              ---         else:
    BLOCO 3                         ---             BLOCO 3
'''
'''nome = str(input('Qual é seu nome? '))
if nome == 'Leo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana': # Possibiliva verificar vários nomes 
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))'''
'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

VARIAVEIS COMPOSTAS (TUPLAS)
- As TUPLAS são IMUTÁVEIS
- Toda tupla é representada com parenteses, apartir do Python5 não é necessário nem colocar parenteses
- As variáveis compostas podem ser representadas:
    - ( ) Entre parenteses são TUPLAS
    - [ ] Entre colchetes são LISTAS
    - { } Entre chaves são DICIONÁRIOS
'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3])'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')


print('->-' *20)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

print('->-' *20)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posição}')
print('Comi pra caramba')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(sorted(lanche))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(f'TUPLA A = {a}')
print(f'TUPLA B = {b}')
print(f'TUPLA C = {c}')
print(f'Comprimento da tupla C = {len(c)}')
print(f'Quantas vezes está aparecendo o número 5 dentro da tupla c? {c.count(5)}')
print(f'Quantas vezes está aparecendo o número 5 dentro da tupla c? {c.count(9)}')
print(f'Em que posição está a primeira ocorrência do numero 8? {c.index(8)}')
print(f'Em que posição está a primeira ocorrência do numero 2? {c.index(2)}')
print(f'Em que posição está a primeira ocorrência do numero 5? {c.index(5)}')
print(f'Em que posição está a segunda ocorrência do numero 5? {c.index(5, 1)}')'''

pessoa = ('Gustavo', 39, 'M', 99.88)
#del(pessoa)#comando DEL deleta a variavel
print(pessoa)
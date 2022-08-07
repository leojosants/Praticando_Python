'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais'''

'''VARIÁVEIS COMPOSTAS (TUPLAS)'''

'''AS TUPLAS SÃO IMUTÁVEIS'''

''' TUPLA CADA ELEMENTO É ENTRE ASPAS SIMPLES E TODOAS ENTRE PARENTESES'''


#lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
#print(f'Lanche : {lanche}')
#print(f'Fatiamento: Na posição zero temos: {lanche[0]}') # OU {LANCHE[-4]}
#print(f'Fatiamento: Na posição menos quatro temos: {lanche[-4]}')
#print(f'Fatiamento: Na posição um temos: {lanche[1]}')
#print(f'Fatiamento: Na posição dois temos: {lanche[2]}')
#print(f'Fatiamento: Na posição três temos: {lanche[3]}')
#print(f'Fatiamento: Verifica do indice zero até o indice dois: {lanche[0:2]}')
#print(f'Fatiamento: Verifica do indice um ate o final: {lanche[1:]}')
#print(f'Fatiamento: Verifica qual é o ultimo elemento: {lanche[-1]}')
#print(f'Fatiamento: Verifica da posição menos dois ate o final, temos: {lanche[-2:]}')
#print(f'Fatiamento: Verifica quantos elementos possui a variavel lanche: {len(lanche)}')


'''for comida in lanche: # ATENÇÃO: Substituir RANGE por LANCHE
    print(f'Eu vou comer: {comida}.')
print('Comi pra caramba!!!')

print('-'*30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer: {lanche[cont]} na posição: {cont}')#verifica a posição/indice de cada elemento
print('Comi pra caramba!!')'''

'''for comida in enumerate(lanche):
    print(f'Eu vou comer: {comida}')

print('-'*40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer: {comida} na posição {pos}')'''

'''print(lanche)
print(f'Os elementos em ordem alfabética é:', sorted(lanche))# organiza em ordem alfabetica em uma lista
print(len(sorted(lanche)))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
#c = a + b # A + B NÃO É A MESMA COISA QUE A + B.
c = b + a # B =A NÃO É A MESMA COISA QUE B + A.
print('\033[7mATENÇÃO: (A+B) NÃO É O MESMO QUE (B+A) !!!!!\033[m')
print(f'A Tupla "a" possui: {a}')
print(f'A Tupla "b" possui: {b}')
print(f'A Tupla "c" possui: {c}')# ocorre a soma de todos os elementos, inclusive repetindo-os
print(f'Na Tupla "C", contem os elementos: {c}')
print(f'A Tupla "C", possui {len(c)} elementos.')
print(f'Quantas vezes aparece o número "5" na Tupla "C": {c.count(5)} vezes.')
print(f'Quantas vezes aparece o número "9" na Tupla "C": {c.count(9)} vezes.')
print(f'Em que posição está o número "8" na tupla "C": {c.index(8)}')
print(f'O elemento "5" aparece em qual posição, a partir da posição "0": {c.index(5, 1)}') # Verifica apartir da primeira posição'''

'''pessoa = ('Gustavo', 39, 'M', 99.88)
#del pessoa #comando que delete qualquer TUPLA, somente ela inteira e não somente alguns elementos
print(f'Na Tupla "pessoa" temos: {pessoa}')'''